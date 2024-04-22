import PySimpleGUI as sg
import serial
import time
import sys

# Initialize Serial Connection
serial_port = '/dev/ttyUSB0'
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate)

# Function to send G-code to the printer
def send_gcode(command):
    ser.write(command.encode('utf-8'))
    ser.write(b'\n')
    time.sleep(0.1)

# Initial positions
INITIAL_X, INITIAL_Y, INITIAL_Z = 200, 150, 170

# Global variables with initial, minimum, and maximum values
X, Y, Z = INITIAL_X, INITIAL_Y, INITIAL_Z
MAX_X, MAX_Y, MAX_Z = 200, 150, 170
MIN_X, MIN_Y, MIN_Z = 0, 0, 0

# Time of the last click and click interval in seconds
last_click_time = 0
click_interval = 0.5

# Function to update the global variables with limit checks, rounding, and action execution
def update_axis(axis, increment):
    global X, Y, Z

    new_value = round((X if axis == 'X' else Y if axis == 'Y' else Z) + increment, 2)
    if MIN_X <= new_value <= MAX_X and axis == 'X' or \
       MIN_Y <= new_value <= MAX_Y and axis == 'Y' or \
       MIN_Z <= new_value <= MAX_Z and axis == 'Z':
        if axis == 'X':
            X = new_value
        elif axis == 'Y':
            Y = new_value
        elif axis == 'Z':
            Z = new_value
        send_gcode(f"G1 {axis}{new_value}")
    else:
        print(f"{axis} axis limit reached.")

    print(f"Updated values: X-{X}, Y-{Y}, Z-{Z}")

def home_printer():
    global X, Y, Z
    send_gcode('G28')  # Homing command
    print('Homing Printer, please do wait for countdown to complete')
    X, Y, Z = INITIAL_X, INITIAL_Y, INITIAL_Z
    for remaining in range(10, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")
    print(f"Printer homed. Reset positions to X: {X}, Y: {Y}, Z: {Z}")
    
# Layout for the Radio Buttons and action buttons
layout = [
    [sg.Radio('X Axis', 'AXIS_CHOICE', key='X', default=True),
     sg.Radio('Y Axis', 'AXIS_CHOICE', key='Y'),
     sg.Radio('Z Axis', 'AXIS_CHOICE', key='Z')],
    
    [sg.Button('+ 0.1 mm', key='+0.1'), sg.Button('+ 1 mm', key='+1'), sg.Button('+ 10 mm', key='+10')],
    [sg.Button('- 0.1 mm', key='-0.1'), sg.Button('- 1 mm', key='-1'), sg.Button('- 10 mm', key='-10')],
    [sg.Button('Home Printer', key='-HOME-')]
]

# Create the window
window = sg.Window('XYZ Control Panel', layout)

# sleep and home
print("Loading printer...")
time.sleep(5)
home_printer()

# Event loop

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in ('+0.1', '+1', '+10', '-0.1', '-1', '-10'):
        current_time = time.time()
        if current_time - last_click_time < click_interval:
            sg.popup('\n\n\n\n\nClicked too fast!\n\n\n\n\n', title='Warning')
        else:
            selected_axis = 'X' if values['X'] else 'Y' if values['Y'] else 'Z'
            increment = float(event.replace(' mm', '').replace('+', ''))
            update_axis(selected_axis, increment)
            last_click_time = current_time

    elif event == '-HOME-':
        home_printer()

# Close the window and serial connection
window.close()
ser.close()

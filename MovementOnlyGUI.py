import PySimpleGUI as sg
import time

# Global variables with initial, minimum, and maximum values
X, Y, Z = 200, 150, 170
MAX_X, MAX_Y, MAX_Z = 200, 150, 170
MIN_X, MIN_Y, MIN_Z = 0, 0, 0

# Time of the last click and click interval in seconds
last_click_time = 0
click_interval = 0.5

# Function to update the global variables with limit checks, rounding, and action execution
def update_axis(axis, increment):
    global X, Y, Z

    if axis == 'X':
        new_value = round(X + increment, 2)
        if MIN_X <= new_value <= MAX_X:
            X = new_value
            # Insert your action code for X axis here
        else:
            print(f"{axis} axis limit reached.")
    elif axis == 'Y':
        new_value = round(Y + increment, 2)
        if MIN_Y <= new_value <= MAX_Y:
            Y = new_value
            # Insert your action code for Y axis here
        else:
            print(f"{axis} axis limit reached.")
    elif axis == 'Z':
        new_value = round(Z + increment, 2)
        if MIN_Z <= new_value <= MAX_Z:
            Z = new_value
            # Insert your action code for Z axis here
        else:
            print(f"{axis} axis limit reached.")

    print(f"Updated values - X: {X}, Y: {Y}, Z: {Z}")

# Layout for the Radio Buttons and action buttons
layout = [
    [sg.Radio('X Axis', 'AXIS_CHOICE', key='X', default=True),
     sg.Radio('Y Axis', 'AXIS_CHOICE', key='Y'),
     sg.Radio('Z Axis', 'AXIS_CHOICE', key='Z')],
    
    [sg.Button('+ 0.1 mm', key='+0.1'), sg.Button('+ 1 mm', key='+1'), sg.Button('+ 10 mm', key='+10')],
    [sg.Button('- 0.1 mm', key='-0.1'), sg.Button('- 1 mm', key='-1'), sg.Button('- 10 mm', key='-10')]
]

# Create the window
window = sg.Window('XYZ Control Panel', layout)

# Event loop
while True:
    event, values = window.read()

    # Close the program if user closes window
    if event == sg.WIN_CLOSED:
        break

    # Handle button clicks for increments and decrements
    if event in ('+0.1', '+1', '+10', '-0.1', '-1', '-10'):
        current_time = time.time()
        if current_time - last_click_time < click_interval:
            sg.popup('Clicked too fast!', title='Warning')
        else:
            selected_axis = 'X' if values['X'] else 'Y' if values['Y'] else 'Z'
            increment = float(event.replace(' mm', ''))
            update_axis(selected_axis, increment)
            last_click_time = current_time  # Update the last click time

# Close the window
window.close()

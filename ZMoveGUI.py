import PySimpleGUI as sg
import serial #printer to pi connection
from time import sleep # pauses in between commands
#from picamera import PiCamera # tools to create camera objects
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
#Connections
serial_port = '/dev/ttyUSB0' # /dev/ttyUSB0 is default for pi, find port name for non pi devices
baud_rate = 115200 # Varies per printer, check manufacturers settings. Anycubic I MegaS = 250000.
#ser = serial.Serial(serial_port, baud_rate)

#Camera
#camera = PiCamera() # initializes new camera object

"""def show_camera():
    camera.resolution = (1920,1080) # 480x360 resolution
    # create smaller preview window
    preview_x = 1240
    preview_y = 600
    preview_width = 640
    preview_height = 480
    camera.rotation = 0
    camera.preview_fullscreen = False
    camera.preview_window = (preview_x, preview_y, preview_width, preview_height)
    camera.start_preview() #begins camera preview
    sleep(2)
    
show_camera() #begins camera, persistent until closed
Movement
def send_gcode(command):
    ser.write(command.encode('utf-8'))
    ser.write(b'\n')
    sleep(0.1)
def home():
    send_gcode('G28') #moves printer to home
    sleep(5)

        
home()
"""

#Starting positions, if printer manually moved, will ne to end and rerun
X_Position = 200.0
Y_Position = 150.0
Z_Position = 170.0

#GUI
def create_choice_buttons(choice):
    return [sg.Button(f'+0.1 {choice}', key=f'+0.1_{choice}'),
            sg.Button(f'+1 {choice}', key=f'+1_{choice}'),
            sg.Button(f'+10 {choice}', key=f'+10_{choice}')]# Define the Layout

tab_layout = [
    [sg.Text('Z-Distance Adjuster')],
    [sg.Button('Z + 1mm', key='-ACTION1-')],
    [sg.Button('Z - 1mm', key='-ACTION2-')]
]

# Define th elayout of the window
layout = [
    [sg.Radio('X', 'CHOICE', key='X', default=True), *create_choice_buttons('X')],
    [sg.Radio('Y', 'CHOICE', key='Y'), *create_choice_buttons('Y')],
    [sg.Radio('Z', 'CHOICE', key='Z'), *create_choice_buttons('Z')]
]

#Create the window
window = sg.Window('Window with Single Tab and Actions', layout)

# Event Loop
while True:
    event, values = window.read()
    #End program if user closes window
    if event == sg.WIN_CLOSED:
        break
    elif event == '-ACTION1-':
        Z_Position += 1.0
        send_gcode("G1Z" + str(Z_Position))
        sg.popup('The current Z-position is: ' + str(Z_Position))
    elif event == '-ACTION2-':
        Z_Position -= 1.0
        print(Z_Position)
        send_gcode("G1Z" + str(Z_Position))
        sg.popup('The current Z-position is: ' + str(Z_Position))

# Close the window
window.close()
        
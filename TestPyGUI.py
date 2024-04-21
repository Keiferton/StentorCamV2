import PySimpleGUI as sg
import io
from PIL import Image, ImageTk
import threading
import time
import picamera

# Function toupdate the camera feed
def update_camera(window,camera):
    while True:
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        image = Image.open(stream)
        photo = ImageTk.PhotoImage(image)
        window['-IMAGE-'].update(data=photo)
        time.sleep(0.1) # adjust as needed
        
# Initialize Camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)

#Define the layout for Tab 1
tab1_layout = [
    [sg.Image(key='-IMAGE-')]
]

#Define the layout for Tab 2
tab2_layout = [
    [sg.Text('This is inside Tab 2')],
    [sg.InputText()],
    [sg.Button('Tab 2 Button')]
]

# Define the layout for the tabs
tab_group_layout = [
    sg.Tab('Camera Feed', tab1_layout, key='-TAB1-'),
    sg.Tab('Tab 2', tab2_layout, key='-TAB2-')
]
    

# Define the main window's contents (layout)
layout = [
    [sg.TabGroup([tab_group_layout], tab_location='top')],
    [sg.Button('Exit', key='-EXIT-')]
]
        

#Create the window
window = sg.Window('Windows with Camera Feed', layout)

# Star camera update Thread
thread = threading.Thread(target=update_camera, args=(window, camera), daemon=True)
thread.start()

# Event loop
while True:
    event, values = window.read(timeout=20)
    if event in (sg.WIN_CLOSED, '-EXIT-'):
        break
    
    
    """if event == sg.WIN_CLOSED:
        break
    elif event == '-MAIN-BUTTON-':
        sg.popup('You clicked the main button!')
    elif event == 'Tab 1 Button':
        sg.popup('You clicked the button on Tab 1!')
    elif event == 'Tab 2 Button':
        sg.popup('You clicked the button on Tab 2!')
"""
#close the winow
window.close()
camera.close()
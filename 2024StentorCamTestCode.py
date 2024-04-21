""" 
Autofocusing Algorithm,
Objectives: 
1. Connect to printer DONE
2. Move printer using G-Code DONE
3. Create Camera Object DONE
4. Move Printer using G-code while camera persists DONE
5. Run Z-stack, capture images, save images in sequential naming format YOU ARE HERE 
6. Export or pass photos through function (method) to apply gabor filter
7. Associate gabor score with z distance. 
8. Create post-gabor function (method) that DOES NOT HOME "NO G28"
9. Run smaller Z stack function (method)
10. Repeat until in focus values are consistently achieved 

Issues: 10/9/2023 - i increments up to 10 too fast (resolved): sleep timer implemented to allow ample time to home
1/22/2024 resolved unlevel camera, had to hold in place while tightening
Authors: 
Keith Curry
San Francisco State University
"""

import serial #printer to pi connection
from time import sleep # pauses in between commands
from picamera import PiCamera # tools to create camera objects
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
#Connections
serial_port = '/dev/ttyUSB0' # /dev/ttyUSB0 is default for pi, find port name for non pi devices
baud_rate = 115200 # Varies per printer, check manufacturers settings. Anycubic I MegaS = 250000.
ser = serial.Serial(serial_port, baud_rate)

#Camera
camera = PiCamera() # initializes new camera object

def show_camera():
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

#Starting positions
global X_Position = 200.0, Y_Position = 150.0, Z_Position = 170.0


#Movement
def send_gcode(command):
    ser.write(command.encode('utf-8'))
    ser.write(b'\n')
    sleep(0.1)
def home():
    send_gcode('G28') #moves printer to home
    sleep(15)
    
home() # homes printer (x,y,z)mm = (200,150,175)

#G-code loop
while True:
    user_input = input("Enter G-code(Starts at X:200mm Y:150mm Z:170mm, type 'exit' to quit): ").strip().upper()
    if user_input =='EXIT':
        break
    else:
        send_gcode("G1 " + user_input)

sleep(2)
#run_z_stack(num_images)
# config = camera.create_preview_configuration()
camera.close() #ends camera
ser.close() # closes camera port`
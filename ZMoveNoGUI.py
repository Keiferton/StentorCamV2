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
X_Position = 200
Y_Position = 150
Z_Position = 170


#Movement
def send_gcode(command):
    ser.write(command.encode('utf-8'))
    ser.write(b'\n')
    sleep(0.1)
def home():
    send_gcode('G28') #moves printer to home
    sleep(15)
    
#home() # homes printer (x,y,z)mm = (200,150,175)
Z_Position -= 1
print(Z_Position)

import picamera

def update_camera_settings(camera):
    try:
        r = float(input("Enter Red Gain (e.g., 1.5): "))
        b = float(input("Enter Blue Gain (e.g., 1.2): "))
        iso = int(input("Enter ISO (e.g., 200): "))
        exposure = int(input("Enter Exposure (microseconds, e.g., 100000): "))
        
        camera.awb_gains = (r, b)
        camera.iso = iso
        camera.shutter_speed = exposure
        print("Camera settings updated successfully!")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def main():
    camera = picamera.PiCamera()

    # Initialize camera with recommended settings
    camera.resolution = (1920, 1080)
    camera.awb_mode = 'off'  # Turn off auto white balance
    camera.awb_gains = (1.5, 1.2)
    camera.iso = 200
    camera.shutter_speed = 100000  # 100 ms exposure

    print("Starting camera preview...")
    camera.start_preview(fullscreen=False, window=(100, 100, 640, 480))

    try:
        while True:
            print("\nCurrent settings:")
            print(f"Red Gain: {camera.awb_gains[0]}")
            print(f"Blue Gain: {camera.awb_gains[1]}")
            print(f"ISO: {camera.iso}")
            print(f"Exposure: {camera.shutter_speed}")
            print("\nType new settings to update the camera:")
            update_camera_settings(camera)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        camera.stop_preview()
        camera.close()

if __name__ == "__main__":
    main()

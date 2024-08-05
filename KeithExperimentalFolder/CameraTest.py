import tkinter as tk
from tkinter import ttk
from picamera import PiCamera

camera = PiCamera()

# Initialize camera with recommended settings
camera.resolution = (1920, 1080)
camera.awb_mode = 'off'  # Turn off auto white balance
camera.awb_gains = (1.5, 1.2)
camera.iso = 200
camera.shutter_speed = 100000  # 100 ms exposure

def update_camera_settings():
    try:
        r = float(red_entry.get())
        b = float(blue_entry.get())
        iso = int(iso_entry.get())
        exposure = int(exposure_entry.get())
        
        camera.awb_gains = (r, b)
        camera.iso = iso
        camera.shutter_speed = exposure
        status_label.config(text="Camera settings updated successfully!")
    except ValueError:
        status_label.config(text="Invalid input. Please enter valid numbers.")

# Function to handle window close event
def on_closing():
    camera.stop_preview()
    camera.close()
    root.destroy()

# Function to show camera preview
def show_camera_preview():
    camera.start_preview()

# Create the main window
root = tk.Tk()
root.title('PiCamera Test Program')
root.protocol("WM_DELETE_WINDOW", on_closing)

# Create the tab control
tab_control = ttk.Notebook(root)

# Picture tab
picture_tab = ttk.Frame(tab_control)
tab_control.add(picture_tab, text='Picture')

# Entries for RGB, ISO, and Exposure
tk.Label(picture_tab, text="Red Gain:").pack(pady=5)
red_entry = tk.Entry(picture_tab)
red_entry.insert(0, "1.5")
red_entry.pack(pady=5)

tk.Label(picture_tab, text="Blue Gain:").pack(pady=5)
blue_entry = tk.Entry(picture_tab)
blue_entry.insert(0, "1.2")
blue_entry.pack(pady=5)

tk.Label(picture_tab, text="ISO:").pack(pady=5)
iso_entry = tk.Entry(picture_tab)
iso_entry.insert(0, "200")
iso_entry.pack(pady=5)

tk.Label(picture_tab, text="Exposure (microseconds):").pack(pady=5)
exposure_entry = tk.Entry(picture_tab)
exposure_entry.insert(0, "100000")
exposure_entry.pack(pady=5)

# Update camera settings button
update_button = tk.Button(picture_tab, text="Update Camera Settings", command=update_camera_settings)
update_button.pack(pady=20)

# Show camera preview button
preview_button = tk.Button(picture_tab, text="Show Camera Preview", command=show_camera_preview)
preview_button.pack(pady=20)

# Status label
status_label = tk.Label(picture_tab, text="")
status_label.pack(pady=5)

# Pack the tab control
tab_control.pack(expand=1, fill='both')

# Start the Tkinter event loop
root.mainloop()

# Close camera when the program ends
camera.close()

import subprocess
import time
import wmi
from plyer import notification

# Name of your Xbox controller (you may need to adjust this)
XBOX_CONTROLLER_NAME = "Xbox Wireless Controller"

def is_xbox_controller_connected():
    wmi_service = wmi.WMI()
    bluetooth_devices = wmi_service.Win32_PnPEntity(Name=XBOX_CONTROLLER_NAME)

    # Debugging: Print device details to see what's available
    if not bluetooth_devices:
        print("No devices found.")
        return False

    for device in bluetooth_devices:
        print(f"Device Found: {device.Name}")
        print(f"Description: {device.Description}")
        print(f"Status: {device.Status}")
        print(f"PNPDeviceID: {device.PNPDeviceID}\n")

        # Simplified connection check, remove the "Connected" filter
        if "Bluetooth" in device.Description:
            return True

    return False

def launch_steam_big_picture():
    subprocess.run(["start", "steam://open/bigpicture"], shell=True)

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Xbox Controller Monitor",
        timeout=5  # Notification will disappear after 5 seconds
    )

if __name__ == "__main__":
    # Delay at startup (e.g., 30 seconds) to allow services to initialize
    time.sleep(30)

    while True:
        if is_xbox_controller_connected():
            show_notification("Xbox Controller", "Xbox controller connected! Launching Steam Big Picture...")
            launch_steam_big_picture()
            break
        else:
            print("Controller not found. Scanning again...")

        # Wait 10 seconds before checking again
        time.sleep(10)

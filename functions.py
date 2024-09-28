import subprocess
import time
import wmi
from plyer import notification

# Name of your Xbox controller (you may need to adjust this)
XBOX_CONTROLLER_NAME = "Xbox Wireless Controller"


def is_xbox_controller_connected():
    wmi_service = wmi.WMI()
    bluetooth_devices = wmi_service.Win32_PnPEntity(Name=XBOX_CONTROLLER_NAME)

    for device in bluetooth_devices:
        # Checking if it's a Bluetooth device with the given name
        if "Bluetooth" in device.Description:
            print("Controller connected!")
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
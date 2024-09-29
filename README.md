# Xbox Controller Auto-Launcher for Steam Big Picture

This script monitors the connection of an Xbox Wireless Controller via Bluetooth and automatically launches Steam Big Picture Mode when the controller connects. The script runs at system startup and checks for the controller's connection every few seconds, only running once per session.

## Prerequisites

### Python Libraries
You will need the following Python libraries installed on your system:
1. **WMI** for accessing Bluetooth device information
2. **Plyer** for showing system notifications

Install them using the following command:
```
pip install wmi plyer
```
### Additional Requirements
Steam must be installed on your system.
Your Xbox controller must be Bluetooth-compatible.
Setup Instructions
Clone or Download the Script: Download the xbox_controller_auto_launcher.py script from this repository to your local machine.

### Create a .bat file:

Create a batch file to run the Python script on startup:

Open Notepad and type the following:

```
@echo off
pythonw C:\path\to\your\script\xbox_controller_auto_launcher.py
```
Replace C:\path\to\your\script\xbox_controller_auto_launcher.py with the actual path to the Python script on your computer.
Save the file with a .bat extension, such as launch_steam_on_controller.bat.
Move the .bat File to the Startup Folder:


Press Win + R and type shell:startup, then press Enter. This opens the Windows Startup folder.
Move the .bat file into this folder. This ensures the script runs automatically when your PC boots.
Test the Script:

Restart your PC.
Once the system starts, the script will begin running in the background. When you turn on and connect your Xbox controller via Bluetooth, Steam Big Picture Mode will automatically launch.
A notification will appear stating "Xbox controller connected! Launching Steam Big Picture."
### Notes
The script will continuously monitor for the controller connection after startup and will only launch Steam Big Picture once per session.
If Steam Big Picture Mode is launched, the script will terminate and won't run again until the PC is restarted.

Let me know if you want to include any additional information!

import time
from functions import is_xbox_controller_connected, show_notification,launch_steam_big_picture


if __name__ == "__main__":
    # Delay at startup (e.g., 30 seconds) to allow services to initialize
    time.sleep(30)

    controller_launched = False  # This flag ensures Steam is only launched once

    while not controller_launched:
        if is_xbox_controller_connected():
            show_notification("Xbox Controller", "Xbox controller connected! Launching Steam Big Picture...")
            launch_steam_big_picture()
            controller_launched = True  # Set the flag to stop further checks
            break  # Exit the loop after launching Steam Big Picture
        else:
            print("Controller not found. Scanning again...")

        # Wait 10 seconds before checking again
        time.sleep(10)
    
    print("Script finished. Steam Big Picture was launched once this session.")

# Wireless ADB Connection Script

This script automates the process of connecting to an Android device via ADB over Wi-Fi, specifically targeting a Wi-Fi hotspot's gateway IP address. It also ensures that any other existing Wi-Fi ADB connections are disconnected, leaving only the desired connection active.

## Prerequisites

* **Android Device:**
    * Developer options enabled.
    * Wireless debugging enabled (or USB debugging, if using older Android versions).
    * Android device hotspot enabled.
* **Windows Computer:**
    * Android SDK Platform-Tools installed (containing `adb.exe`) and added to your system's PATH environment variable.
    * Python installed (available through the Microsoft Store or a standard installation) and added to your system's PATH environment variable.
* **Wi-Fi Connection:**
    * Your windows computer must be connected to the Android device's hotspot.

## Files

* `wireless_adb.bat`: The main batch script that orchestrates the connection process.
* `get_gateway_ip.py`: A Python script that extracts the gateway IP address from `ipconfig` output.
* `confi.txt`: A temporary file that stores the output of the `ipconfig` command.
* `gateway_ip.txt`: A temporary file that stores the extracted gateway IP address.

## Usage

1.  **Prepare your Android device:**
    * Enable the hotspot.
    * Enable wireless debugging on your android device.
2.  **Connect your Windows computer:**
    * Connect your Windows computer to the Android device's hotspot.
3.  **Run the script:**
    * Double-click `wireless_adb.bat` or run it from the command prompt.

## Script Workflow

1.  **Capture `ipconfig` Output:**
    * The `wireless_adb.bat` script executes `ipconfig` and saves the output to `confi.txt`.
2.  **Extract Gateway IP:**
    * The batch script then runs `get_gateway_ip.py`, which reads `confi.txt`, parses the output, and extracts the gateway IP address. The IP address is saved to `gateway_ip.txt`.
3.  **Check for Errors:**
    * The batch script reads the gateway IP from `gateway_ip.txt`. If the content is "Error", the script exits.
4.  **Connect to ADB:**
    * The script uses `adb tcpip 5555` to enable ADB over Wi-Fi.
    * It then uses `adb connect [gateway_ip]:5555` to establish the connection.
5.  **Disconnect Other Wi-Fi ADB Connections:**
    * The script runs `adb devices` and disconnects any other devices connected via Wi-Fi ADB (port 5555) that do not match the current gateway IP.
6.  **Display Connected Devices:**
    * The script runs `adb devices` again to display the updated list of connected devices.
7.  **Cleanup:**
    * The temporary files `confi.txt` and `gateway_ip.txt` are deleted.
8.  **Python Check:**
    * The script checks if python is installed, and if not, displays an error message.

## Troubleshooting

* **"Python is not installed" error:**
    * Ensure that Python is installed and added to your system's PATH environment variable.
* **Connection issues:**
    * Verify that your Android device's hotspot is active and that your Windows computer is connected to it.
    * Ensure that wireless debugging is enabled on your android device.
    * Check that the Android SDK Platform-Tools are installed and added to your PATH.
    * If using wireless debugging, ensure the android device has been paired.
* **Firewall:**
    * Ensure that your firewall is not blocking ADB connections.
* **Incorrect Gateway IP:**
    * If the script is not detecting the correct gateway IP, ensure that the "Wireless LAN adapter Wi-Fi:" portion of the ipconfig output matches the script. If it does not, the python script will need to be modified.

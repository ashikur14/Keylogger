Keylogger with Remote Logging to Flask Server

Author: Ashikur Rahman
Purpose: Educational project for learning keylogging and network communication. Do not use on unauthorized devices.

Project Overview

This project demonstrates how to capture keystrokes on a computer using Python and send the captured data to a remote host running a Flask server. The host in this project is a Termux environment on an Android device.

Key Features:

Captures keyboard input using pynput.

Sends keystrokes to a remote server using HTTP POST requests.

Server receives keystrokes and logs them to a text file (received_keys.txt).

Fully configurable for testing on your own devices or lab setup.

Disclaimer

⚠️ Important: This keylogger is strictly for educational and testing purposes. Using this on devices without explicit permission is illegal and considered malicious activity. Only run this project on devices you own.

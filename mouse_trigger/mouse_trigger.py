"""
Send a trigger to the Arduino every time you click the mouse.

    pip install pyserial pynput
    python mouse_trigger.py COM3          (Windows)
    python mouse_trigger.py /dev/ttyACM0  (Linux)

Press Esc to quit.
"""
import sys
import time

import serial
from pynput import keyboard, mouse

PORT = sys.argv[1] if len(sys.argv) > 1 else "COM3"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.1)
time.sleep(2)  # the Arduino resets when the port opens, give it a moment
print(f"Connected to {PORT}. Click to send a trigger, Esc to quit.")


def on_click(x, y, button, pressed):
    if pressed:  # only on press, not on release
        ser.write(b"T")
        reply = ser.readline().decode(errors="ignore").strip()
        print(f"{time.strftime('%H:%M:%S')}  {button.name} click -> trigger sent ({reply or 'no reply'})")


def on_key(key):
    if key == keyboard.Key.esc:
        mouse_listener.stop()
        return False


mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()
with keyboard.Listener(on_press=on_key) as k:
    k.join()

ser.close()
print("Closed.")

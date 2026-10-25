import pyautogui as auto
import time

while True:
    time.sleep(1)
    x, y = auto.position()
    print(f"Your mouse is in: x={x}, y={y}")
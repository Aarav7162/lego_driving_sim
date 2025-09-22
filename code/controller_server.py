import pygame
import requests
from pynput.keyboard import Controller
import time

keyboard = Controller()
pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for js in joysticks: js.init()

def select_controller():
    print("Press RT or LT to select controller...")
    selected = None
    while selected is None:
        for js in joysticks:
            pygame.event.pump()
            rt = js.get_axis(5)
            lt = js.get_axis(2)
            if rt > 0.1 or lt > 0.1:
                selected = js
                print(f"Controller {js.get_name()} selected")
                return selected
        time.sleep(0.1)

controller = select_controller()

def get_brake_value():
    try:
        r = requests.get("https://iot.roboninja.in/index.php?action=read&UID=YOUR_UID&braking_value")
        return float(r.text)
    except:
        return 0.0

def calibrate(value, min_val=-1.0, max_val=1.0):
    value = max(min(value, max_val), min_val)
    return (value - min_val) / (max_val - min_val)

while True:
    pygame.event.pump()
    brake_val = get_brake_value()
    rt_scaled = calibrate(controller.get_axis(5))
    lt_scaled = calibrate(controller.get_axis(2))
    if brake_val > 0.05 or rt_scaled > 0.05:
        keyboard.press('s')
    else:
        keyboard.release('s')
    if lt_scaled > 0.05:
        keyboard.press('d')
    else:
        keyboard.release('d')
    time.sleep(0.01)

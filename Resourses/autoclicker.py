import mouse
import keyboard
import time

isclicking = False

def switcher():
    global isclicking
    isclicking = not isclicking

def breaker():
    break

keyboard.add_hotkey('p',switcher)
keyboard.add_hotkey('o', breaker)

while True:
    if isclicking:
        mouse.click(button = 'left')
    time.sleep(0.000001)
import pyautogui as p
import time

while True:
    time.sleep(1)
    try:
        x = p.locateCenterOnScreen('shark.png',confidence=0.9)
        print(x)
    except:
        print('not found')


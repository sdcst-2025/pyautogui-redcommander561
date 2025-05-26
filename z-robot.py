import pyautogui as p
import time

while True:
    time.sleep(1)
    try:
        x = p.locateCenterOnScreen('unlocked uprgrade 1.png',confidence=0.9)
        print(x)
    except:
        print('not found')

#(443,413)





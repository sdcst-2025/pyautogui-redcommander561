import pyautogui
import time
import os

try:
    while True:
        
        x, y = pyautogui.position()
        
       
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"Mouse position: X={x}, Y={y}")
        
       
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nTracking stopped.")


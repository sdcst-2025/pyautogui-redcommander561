import pyautogui as p
import time

brainrot = (443,413)




upgrade_new_img = 'newest_upgrade.png'
upgrade_old_img = 'older_upgrade.png'
brainrot_img = 'brainrot_character.png'

def click_max_times(duration=2, interval=0.05):
    """Click repeatedly for the given duration and interval."""
    start = time.time()
    while time.time() - start < duration:
        p.click()
        time.sleep(interval)

def find_and_click_upgrade(upgrade_img):
    """Locate upgrade on screen and click it repeatedly until it disappears (locked)."""
    while True:
        location = p.locateOnScreen(upgrade_img, confidence=0.7)
        if location is None:
            
            break
        p.moveTo(p.center(location))
        p.click()
        time.sleep(0.1)

def main():
    while True:
        
        brainrot_location = p.locateOnScreen(brainrot_img, confidence=0.7)
        if brainrot_location:
            p.moveTo(p.center(brainrot_location))
            click_max_times(duration=2, interval=0.05)

        
        new_upgrade_loc = p.locateOnScreen(upgrade_new_img, confidence=0.7)
        old_upgrade_loc = p.locateOnScreen(upgrade_old_img, confidence=0.7)

        if new_upgrade_loc and old_upgrade_loc:
            
            find_and_click_upgrade(upgrade_new_img)

            
            next_upgrade_loc = p.locateOnScreen(upgrade_old_img, confidence=0.7)
            if next_upgrade_loc:
                p.moveTo(p.center(next_upgrade_loc))
                find_and_click_upgrade(upgrade_old_img)

            
            if brainrot_location:
                p.moveTo(p.center(brainrot_location))

        time.sleep(0.5)  

if __name__ == "__main__":
    print("Starting Italian Brainrot clicker...")
    main()




#(443,413)





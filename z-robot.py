import pyautogui as p
import time

brainrot = (443, 413)


locked1 = 'locked-upgrade-1.png'
locked2 = 'locked-upgrade-2.png'
locked3 = 'locked-upgrade-3.png'
upg3 = 'unlocked-upgrade-3.png'  
upg2 = 'unlocked-upgrade-2.png'
upg1 = 'unlocked-upgrade-1.png'


def click(duration=2, interval=0.05):
    start = time.time()
    while time.time() - start < duration:
        p.click()
        time.sleep(interval)

def find(upgrade_img):
    while True:
        location = p.locateOnScreen(upgrade_img, confidence=0.7)
        if location is None:
            break
        p.moveTo(p.center(location))
        p.click()
        time.sleep(0.1)

def main():
    while True:
        brainrot_location = (443, 413)
        if brainrot_location:
            p.moveTo(brainrot_location)
            click(duration=2, interval=0.005)

        new_upgrade_loc = p.locateOnScreen(upg3, confidence=0.7)
        old_upgrade_loc = p.locateOnScreen(upg2, confidence=0.7)

        if new_upgrade_loc and old_upgrade_loc:
            find(upg3)
            if not upg3:
                find(upg2)
            next_upgrade_loc = p.locateOnScreen(upg2, confidence=0.7)
            if next_upgrade_loc:
                p.moveTo(p.center(next_upgrade_loc))
                find(upg2)

            upgrade_loc = p.locateOnScreen(upg1, confidence=0.7)
            if upgrade_loc:
                p.moveTo(p.center(upgrade_loc))
                find(upg1)

        if 'next_upgrade_loc' in locals() and 'upgrade_loc' in locals():
            find(upg2)
            if not upg2:
                find(upg1)

            if brainrot_location:
                p.moveTo(brainrot_location)

        time.sleep(0.5)

if __name__ == "__main__":
    print("Starting Italian Brainrot clicker...")
    main()

#fix so when I can't upgrade upgrade 3 anymore, and becomes locked-upgrade-3, tries upgrade 2, and if it cant find that then upgrade 1, then back to clicking
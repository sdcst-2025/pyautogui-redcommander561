import pyautogui as p
import time

brainrot = (443, 413)


upgrades_coords = [
    (846, 290),
    (855, 375),
    (852, 454),
    (868,559)
]

def click(duration=2, interval=0.05):
    start = time.time()
    while time.time() - start < duration:
        p.click()
        time.sleep(interval)

def click_upgrade(coord, times=5):
    p.moveTo(coord)
    for _ in range(times):
        p.click()
        time.sleep(0.1)

def main():
    print("Starting Italian Brainrot clicker in 3 seconds...")
    time.sleep(3)

    while True:
        print("Clicking brainrot...")
        p.moveTo(brainrot)
        click(duration=2, interval=0.005)

        print("Clicking upgrades...")
        for coord in upgrades_coords:
            click_upgrade(coord, times=5)

       
        p.moveTo(brainrot)

        time.sleep(0.5)

if __name__ == "__main__":
    main()

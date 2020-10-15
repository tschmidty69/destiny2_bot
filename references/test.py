"""

Python v3.8.1

Author: pyFlummox version: 1.2.0.1 -

Description: This program is designed to launch forges in Destiny 2 as you now go to orbit each time you finish a forge.

Modules used: pyautogui, time

Version update:
added support for 2560 screens.




"""

import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()

print("This is the screenWith: ")
print(screenWidth)

print("\nThis is the screenHeight: ")
print(screenHeight)

if screenWidth == 2560:
    ratio_sub = 3440 / 2560

print("please be in orbit, where the open directory button is visable. \n")

print("Created by: pyFlummox\n")

while True:
    time.sleep(3)
    x = 1720
    y = 1142
    if screenWidth == 2560:
        x = x / ratio_sub
    print("Move to Open Directory ")
    print(x)
    pyautogui.moveTo(x, y)  # Move to Open Directory
    time.sleep(1)
    pyautogui.click(x, y)  # click

    time.sleep(3)
    x = 1727
    y = 777

    if screenWidth == 2560:
        x = x / ratio_sub
    print("Move to the EDZ on map ")
    print(x)

    pyautogui.moveTo(x, y)  # Move to the EDZ on map
    time.sleep(1)
    pyautogui.click(x, y)  # click
    time.sleep(3)
    x = 616
    y = 1301

    if screenWidth == 2560:
        x = 200

    print("move to forge ")
    print(x)
    pyautogui.moveTo(x, y)
    # time.sleep(.05)
    pyautogui.click(x, y)  # move to forge
    time.sleep(2)
    x = 3215
    y = 1187
    if screenWidth == 2560:
        x = x / ratio_sub
    print("move to launch ")
    print(x)
    pyautogui.moveTo(x, y)  # move to launch
    time.sleep(1)
    pyautogui.click(x, y)  # click
    time.sleep(5)
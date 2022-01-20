import pyautogui
from time import sleep

sleep(5)
print(
    f'{pyautogui.position()}, {pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1])}')  # prints the position of the mouse.


sleep(5)
print(pyautogui.pixel(1317, 643))

import pyautogui
import time 

time.sleep(5)
file = open('Spam.txt', 'r')
for word in file:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
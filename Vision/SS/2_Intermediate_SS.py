from PIL import Image 
import pyautogui as pag
import time
import keyboard
time.sleep(3)

filepath  = "/Users/gim-yeonjeong/Desktop/Vision/SS/images"

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")

while True:
    if keyboard.is_pressed("shift"):
        screenshot()
    elif keyboard.is_pressed("esc"):
        break


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:38:11 2022

@author: thorknudsen
"""

from PIL import ImageGrab
import cv2
import numpy as np
import time
import pyautogui

#screenshot = ImageGrab.grab(bbox=(1854, 1222, 1878, 1246))
#screenshot = ImageGrab.grab()
#frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

img = cv2.imread("/Users/thorknudsen/Desktop/playButton.png", cv2.IMREAD_GRAYSCALE)
# img3 = cv2.imread("/Users/thorknudsen/Desktop/img1.png", cv2.IMREAD_GRAYSCALE)


# result = cv2.matchTemplate(img, img3, cv2.TM_CCOEFF_NORMED)
# pos = np.unravel_index(result.argmax(), result.shape)
# pos = np.where(result > 0.98)

if __name__ == '__main__':
    while True:
    #    screenshot = ImageGrab.grab(bbox=(1854, 1222, 1878, 1246))
    #    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    #    if np.allclose(img, frame, atol=20):
    #        pyautogui.click(920,620)

        screenshot = ImageGrab.grab()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
            
        result = cv2.matchTemplate(img, frame, cv2.TM_CCOEFF_NORMED)
        pos = np.unravel_index(result.argmax(), result.shape)
        print(result.max())
        if result.max() > 0.99:
            pyautogui.click(int(pos[1]/2), int(pos[0]/2))

        time.sleep(1)
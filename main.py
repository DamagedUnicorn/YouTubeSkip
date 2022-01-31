#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:38:11 2022

@author: DamagedUnicorn
"""

from PIL import ImageGrab
import cv2
import numpy as np
import time
import pyautogui

refPlayButton = cv2.imread("/Users/thorknudsen/Desktop/playButton.png", cv2.IMREAD_GRAYSCALE)

if __name__ == '__main__':
    while True:
        screenshot = ImageGrab.grab()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
            
        result = cv2.matchTemplate(refPlayButton, frame, cv2.TM_CCOEFF_NORMED)
        pos = np.unravel_index(result.argmax(), result.shape)
        print(result.max())
        if result.max() > 0.99:
            pyautogui.click(int(pos[1]/2), int(pos[0]/2))

        time.sleep(1)
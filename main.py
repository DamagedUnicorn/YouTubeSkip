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

imgPlayButton = cv2.imread("referenceImages/playButton.png", cv2.IMREAD_GRAYSCALE)
imgInfoAndClose = cv2.imread("referenceImages/infoAndClose.png", cv2.IMREAD_GRAYSCALE)

if __name__ == '__main__':
    while True:
        # take screenshot
        screenshot = ImageGrab.grab()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
        
        # check if skip add button is in screenshot
        #result = cv2.matchTemplate(imgPlayButton, frame, cv2.TM_CCOEFF_NORMED)
        #if result.max() > 0.99:
        #    pos = np.unravel_index(result.argmax(), result.shape)
        #    pyautogui.click(int((pos[1] + 12)/2), int((pos[0] + 12)/2))

        # check if close add button is in screen
        result = cv2.matchTemplate(imgInfoAndClose, frame, cv2.TM_CCOEFF_NORMED)
        print(result.max())
        if result.max() > 0.99:
            pos = np.unravel_index(result.argmax(), result.shape)
            pyautogui.moveTo(int((pos[1] + 15)/2), int((pos[0] + 47)/2))

        time.sleep(1)
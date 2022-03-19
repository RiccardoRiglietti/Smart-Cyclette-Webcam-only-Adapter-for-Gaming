#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 00:06:49 2021

@author: riccardo
"""

import cv2
import numpy as np
import cv2.cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
import random
import time
from tkinter import *

root = Tk()
var = StringVar()
label = Label( root, textvariable=var)
label.config(font=("Courier", 74))

var.set("0")
label.pack()
# webcam usb solo a destra
cap = cv2.VideoCapture(2)
cap.set(3, 640//20)
cap.set(4, 480//20)
root.attributes("-topmost", True)

average, last_average = 0,0

counter = 0

print("mousedown initial")
energy = 0
counter = 0
time_last = time.time()
while(1):
    root.update()
    root.lift()

    counter += 1
    var.set(str(energy))


    # Take each frame
    _, frame = cap.read()
    
    average = np.average(frame)
    
    # cv2.imshow('frame',frame)
    print(energy, average)
    if average < 0.6 * last_average and time.time() - time_last > 0.25:
        time_last = time.time()
        print("Trigger")
        energy += 1
        pyautogui.mouseDown()
        # pyautogui.mouseUp()
    #print(frame.shape)
    # how much greener is it than the the other colors
    
    # 0.5 is the difficulty, the higher the more difficult
    # 5 too hard, 6 too easy
    # 6 and 0.03 good difficulty
    if counter % 6 == 0 or random.random() < 0.0039:
        energy -= 1
        energy = 0 if energy < 0 else energy
        if energy <= 0:
            pyautogui.mouseUp()
            
            
    #visual_energy = [[1 if i < energy else 0 for i in range(20)]]
    #plt.close()
    #plt.imshow(visual_energy)
    #plt.show()
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
    last_average = average
cv2.destroyAllWindows()

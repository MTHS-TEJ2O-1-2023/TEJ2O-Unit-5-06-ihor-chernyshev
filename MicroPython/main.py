"""
Created by: Ihor Chernyshev
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *


class HCSR04:
    # this class abstracts out the functionality of the HC-SR04 and
    # returns distance in mm
    # Trig: pin 1
    # Echo: pin 2
    ...


sonar = HCSR04()
display.clear
display.show(Image.HAPPY)

while True:
    display.show(sonar.distance_mm() / 10)
    sleep(500)

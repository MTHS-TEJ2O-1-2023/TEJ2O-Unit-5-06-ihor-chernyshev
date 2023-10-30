"""
Created by: Ihor Chernyshev
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

# setup
from microbit import *
from machine import time_pulse_us

display.clear()
display.show(Image.HAPPY)

tring = pin1
echo = pin2

tring.write_digital(1)
echo.read_digital()

# finding the distance
while True:
    if button_a.was_pressed():
        tring.write_digital(1)
        tring.write_digital(0)
        micros = time_pulse_us(echo, 2)
        t_echo = micros / 1000000
        dist_cm = (t_echo / 2) * 34300
        display.scroll(str(int(dist_cm)))
        display.show(Image.HAPPY)

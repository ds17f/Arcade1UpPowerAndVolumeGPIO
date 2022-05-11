#!/bin/env python3

import RPi.GPIO as GPIO
import time
import subprocess
from datetime import datetime

DEBUG = False

# Setup the GPIO pin numbers
POWER = 5

switches = [POWER]

GPIO.setmode(GPIO.BOARD)

for switch in switches:
    DEBUG and print(switch)
    GPIO.setup(switch, GPIO.IN)

oldButtonState = False

def power_callback(channel):
    global oldButtonState
    buttonState = GPIO.input(POWER)

    if buttonState != oldButtonState and buttonState:
        if DEBUG:
            # Switch is in off position
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"{current_time}: Switched Off")
        DEBUG and print("halting")
        subprocess.call("halt", shell=True)
        DEBUG and print("halted")

    if buttonState != oldButtonState and not buttonState:
        if DEBUG:
            # Switch is in on position
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"{current_time}: Switched On")

    oldButtonState = buttonState


GPIO.add_event_detect(POWER, GPIO.RISING, callback=power_callback)

while(True):
    time.sleep(0.1)


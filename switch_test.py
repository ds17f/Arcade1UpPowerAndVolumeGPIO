#!/bin/env python3

import RPi.GPIO as GPIO
import time
from datetime import datetime


# Setup the GPIO pin numbers
VOL_UP = 27
VOL_DOWN = 4
POWER = 21

switches = [VOL_UP, VOL_DOWN, POWER]

GPIO.setmode(GPIO.BCM)

GPIO.setup(POWER, GPIO.IN)
for switch in switches:
    print(switch)
    GPIO.setup(switch, GPIO.IN)


def power_callback(channel):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{current_time}: Power Pressed")

def vol_up_callback(channel):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{current_time}: Vol Up Pressed")

def vol_down_callback(channel):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{current_time}: Vol Down Pressed")


GPIO.add_event_detect(POWER, GPIO.RISING, callback=power_callback)
GPIO.add_event_detect(VOL_UP, GPIO.RISING, callback=vol_up_callback)
GPIO.add_event_detect(VOL_DOWN, GPIO.RISING, callback=vol_down_callback)

while(True):
    time.sleep(0.1)


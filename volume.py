#!/bin/env python3

import RPi.GPIO as GPIO
import time
from datetime import datetime
import alsaaudio as audio

DEBUG = True

VOLUME_STEP = 5

GPIO.setmode(GPIO.BOARD)

# Setup the GPIO pin numbers
VOL_UP = 12
VOL_DOWN = 16

switches = [VOL_UP, VOL_DOWN]

for switch in switches:
    print(switch)
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# initialize the audio mixer controls

scanCards = audio.cards()
for card in scanCards:
    scanMixers = audio.mixers(scanCards.index(card))
    print("mixers:", scanMixers)

if DEBUG:
    print(f"cards: {scanCards}")

mixer = audio.Mixer("Headphone", cardindex=0)

while(True):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    vol_down_state = GPIO.input(VOL_DOWN)
    vol_up_state = GPIO.input(VOL_UP)

    if not vol_down_state:
        current_volume = mixer.getvolume()
        DEBUG and print(f"{current_time}: Vol: {current_volume} stepping DOWN by {VOLUME_STEP}")
        new_volume = int(current_volume[0]) - VOLUME_STEP
        mixer.setvolume(max([0, new_volume]))

    if not vol_up_state:
        current_volume = mixer.getvolume()
        DEBUG and print(f"{current_time}: Vol: {current_volume} stepping UP by {VOLUME_STEP}")
        new_volume = int(current_volume[0]) + VOLUME_STEP
        mixer.setvolume(min([100, new_volume]))

    time.sleep(0.1)


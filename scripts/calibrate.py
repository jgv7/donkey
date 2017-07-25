"""
calibrate.py

### WARNING: Make sure your car's wheel's are off the groud so it doesn't run away.

Run this script to test what PWM values will work for your car's steering and
throttle control. You'll be promted to enter the channel to test and then enter
PWM test values. Start at ~100 and work your way up until you get the desired result.


Usage:
    calibrate.py

"""
from time import sleep

import donkey as dk


if __name__ == '__main__':

    while True:
        channel = input('What actuator channel: ')
        if channel.isdigit():
            channel = int(channel)
            break
        else:
            print('  ERROR: Must specify integer')
    c = dk.actuators.PCA9685_Controller(channel)

    while True:
        pmw = input('  PMW Value: ')
        if not pmw.isdigit():
            if pmw == 'q': break
            if pmw == 'quit': break
            print('  ERROR: Must specify integer')
            continue

        pmw = int(pmw)
        c.set_pulse(pmw)


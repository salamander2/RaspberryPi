#!/usr/bin/env python
#########################################################
# This program will pulse two LEDs using PWM 
# I've called them "LOne" and "LTwo". These can be assigned to any LED defined below.
#########################################################

__author__ = 'griffin'
import RPi.GPIO as GPIO
import time, thread

# ##global variables
# LED colours go RYGBBGYR
# here are the GPIO pins in the order that they're connected.
B1 = 14
G1 = 15
Y1 = 18
R1 = 23
R2 = 24
Y2 = 25
G2 = 8
B2 = 7

# R1 Y1 G1 B1  B2 G2 Y2 R2
LEDS = [23, 18, 15, 14, 7, 8, 25, 24]

# pin# for switch
# SW1 = 4

pauseTime = 0.02


def setup():
    """setup all pins, etc"""
    global LOne, LTwo
    GPIO.setmode(GPIO.BCM)
    #set all LED pins to be output and internal pul down resistor
    for pin in LEDS:
        GPIO.setup(pin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    #set up switch
    #GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #GPIO.add_event_detect(SW1, GPIO.RISING, callback=modeSelect, bouncetime=300)

    #set up PWM
    LOne = GPIO.PWM(R1,100)
    LTwo = GPIO.PWM(Y1,100)


def flash(n, seq):
    """flash seq n times """
    for i in range(0, n):
        for pin in seq:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        for pin in seq:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)

def main():
    setup()
    flash(5, LEDS[::2] )
    flash(5, LEDS[1::2] )
    GPIO.cleanup()

def main2():
    global LOne,LTwo
    setup()
    LOne.start(0)
    LTwo.start(100)
    try:
        while True:
            for i in range(0,101):      # 101 because it stops when it finishes 100
                LOne.ChangeDutyCycle(i)
                LTwo.ChangeDutyCycle(100 - i)
                time.sleep(pauseTime)
            for i in range(100,-1,-1):      # from 100 to zero in steps of -1
                LOne.ChangeDutyCycle(i)
                LTwo.ChangeDutyCycle(100 - i)
                time.sleep(pauseTime)

    except KeyboardInterrupt:
        LOne.stop()            # stop the LOne output
        LTwo.stop()              # stop the LTwo PWM output
        GPIO.cleanup()          # clean up GPIO on CTRL+C exit

main()
main2()


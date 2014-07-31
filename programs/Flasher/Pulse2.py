#!/usr/bin/env python
#########################################################
# This program will pulse two LEDs using PWM 
# I've called them "LOne" and "LTwo".
#########################################################

__author__ = 'griffin'
import RPi.GPIO as GPIO
import time, thread

# ##global variables

# here are the two LEDs and their GPIO pins the connect to.
LED1 = 23
LED2 = 18

def setup():
    """setup all pins, etc"""
    global LOne, LTwo
    GPIO.setmode(GPIO.BCM)
    #set all LED pins to be output and internal pul down resistor
    GPIO.setup(LED1, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED2, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

    #set up PWM
    LOne = GPIO.PWM(LED1,100)
    LTwo = GPIO.PWM(LED2,100)


def flash(n, pin):
    """flash pin n times """
    for i in range(0, n):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)

def main():
    global LOne,LTwo
    setup()
	#flash each LED 8 times - for fun
    flash(8, LED1)
    flash(8, LED2)

    LOne.start(0)
    LTwo.start(100)

    try:									# try-catch is needed to gracefully handle CTRL-C
        while True:							#endless loop
            for i in range(0,101):     	# 101 because it stops when it finishes 100
                LOne.ChangeDutyCycle(i)
                LTwo.ChangeDutyCycle(100 - i)
                time.sleep(pauseTime)
            for i in range(100,-1,-1):      # from 100 to zero in steps of -1
                LOne.ChangeDutyCycle(i)
                LTwo.ChangeDutyCycle(100 - i)
                time.sleep(pauseTime)

    except KeyboardInterrupt:
        LOne.stop()               # stop the LOne output
        LTwo.stop()              # stop the LTwo PWM output
        GPIO.cleanup()          # clean up GPIO on CTRL+C exit

#now start the program
main()



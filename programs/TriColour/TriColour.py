#!/usr/bin/env python
##############################################################
# This program changes the colour of a Tri-Colour LED
# based on which keys you press.
# Note: this program requires that it be run from a command line.
# Since it uses the terminal, it will not work in Thonny IDE.
# ------------------------------------------------------------
# Update Dec 2020: remove import thread, fix print() statements

__author__ = 'griffin'
import RPi.GPIO as GPIO
import time

# ##global variables
# here are the GPIO pins in the order that they're connected.
B1 = 11
G1= 9 
R1 = 10

pauseTime = 0.02


class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen.
    http://code.activestate.com/recipes/134892/
    http://floss.zoomquiet.io/data/20050627093345/index.html
    """
    def __init__(self):
        import tty
        import sys

    def __call__(self): 
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ch == '\x03':
            raise KeyboardInterrupt
        elif ch == '\x04':
            raise EOFError
        return ch



def setup():
    """setup all pins, etc"""
    global blue, green, red
    GPIO.setmode(GPIO.BCM)
    #set all LED pins to be output
    GPIO.setup(B1, GPIO.OUT)
    GPIO.setup(G1, GPIO.OUT)
    GPIO.setup(R1, GPIO.OUT)

    #set up PWM
    blue = GPIO.PWM(B1,100)
    green = GPIO.PWM(G1,100)
    red = GPIO.PWM(R1,100)


def flash(n, pin):
    """flash seq n times """
    for i in range(0, n):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)

def main():
    setup()
    flash(5, B1)
    flash(5, G1)
    flash(5, R1)
    GPIO.cleanup()

def main2():
    global blue,green,red
    setup()
    bb=0
    gg=0
    rr=0
    blue.start(bb)
    green.start(gg)
    red.start(rr)
    print ("Press r g b to increase brightness")
    print ("Press R G B to decrease brightness")
    print ("Press q or c to quit the program (cancel)\n")
    keypress = _Getch()
    try:
        while True:
            key = keypress()
            if key == 'c' or key == 'C' or key == 'q' or key == 'Q':
                blue.stop()            # stop the white PWM output
                green.stop()            # stop the white PWM output
                red.stop()              # stop the red PWM output
                GPIO.cleanup()          # clean up GPIO on CTRL+C exit
                break
            if key == 'b':
                bb += 5
                if bb > 100: bb = 100
                blue.ChangeDutyCycle(bb)
            if key == 'B':
                bb -= 5
                if bb < 0: bb = 0
                blue.ChangeDutyCycle(bb)
            if key == 'g':
                gg += 5
                if gg > 100: gg = 100
                green.ChangeDutyCycle(gg)
            if key == 'G':
                gg -= 5
                if gg < 0: gg = 0
                green.ChangeDutyCycle(gg)
            if key == 'r':
                rr += 5
                if rr > 100: rr = 100
                red.ChangeDutyCycle(rr)
            if key == 'R':
                rr -= 5
                if rr < 0: rr = 0
                red.ChangeDutyCycle(rr)
            print ("%d %d %d" % (rr, gg, bb) )
            time.sleep(pauseTime)

    except KeyboardInterrupt:   # on CTRL+C ...
        blue.stop()             # stop the PWM output
        green.stop()            # for each LED
        red.stop()              # 
        GPIO.cleanup()          # clean up GPIO 

main2()


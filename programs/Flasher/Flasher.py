#!/usr/bin/env python

__author__ = 'griffin'
import RPi.GPIO as GPIO
import time, thread, subprocess

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
SW1 = 4

#mode variable
mode = 0


def setup():
    """setup all pins, etc"""
    GPIO.setmode(GPIO.BCM)
    #set all LED pins to be output and internal pull down resistor
    for pin in LEDS:
        GPIO.setup(pin, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
    #set up switch.
    #NOTE: the switch must have a Pull UP resistor, because when it is pressed it connects the pin (#4) to the ground.
    # If it is set up as Pull DOWN, then there is no difference between when the switch is pressed or not. 
    # It is at 0 Volts in both cases.
    GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(SW1, GPIO.RISING, callback=modeSelect, bouncetime=300)


def allon():
    for pin in LEDS:
        GPIO.output(pin, GPIO.HIGH)


def alloff():
    for pin in LEDS:
        GPIO.output(pin, GPIO.LOW)


def flash(n, seq):
    """flash seq n times """
    for i in range(0, n):
        for pin in seq:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        for pin in seq:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)


def ripple(n=10):
    """ripple through all LEDs """
    for i in range(0, n):
        for pin in LEDS:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.01)

        for pin in reversed(LEDS):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.01)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.01)


def altern(n=10):
    """alternately flash banks of 4"""
    for i in range(0, n):
        for pin in LEDS[0:4]:
            GPIO.output(pin, GPIO.HIGH)
        for pin in LEDS[4:8]:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.4)
        for pin in LEDS[0:4]:
            GPIO.output(pin, GPIO.LOW)
        for pin in LEDS[4:8]:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.4)

        for pin in LEDS:
            GPIO.output(pin, GPIO.LOW)


def color (n=3):
    """ cycle through pins of same colour """
    allon()
    time.sleep(0.4)
    GPIO.output(B1, GPIO.LOW)
    GPIO.output(B2, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(G1, GPIO.LOW)
    GPIO.output(G2, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(Y1, GPIO.LOW)
    GPIO.output(Y2, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

    for i in range(0, n):
	#red to blue
        GPIO.output(R1, GPIO.HIGH)
        GPIO.output(R2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(R1, GPIO.LOW)
        GPIO.output(R2, GPIO.LOW)
        GPIO.output(Y1, GPIO.HIGH)
        GPIO.output(Y2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(Y1, GPIO.LOW)
        GPIO.output(Y2, GPIO.LOW)
        GPIO.output(G1, GPIO.HIGH)
        GPIO.output(G2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(G1, GPIO.LOW)
        GPIO.output(G2, GPIO.LOW)
        GPIO.output(B1, GPIO.HIGH)
        GPIO.output(B2, GPIO.HIGH)
        time.sleep(0.2)
	#blue to red
        GPIO.output(B1, GPIO.LOW)
        GPIO.output(B2, GPIO.LOW)
        GPIO.output(G1, GPIO.HIGH)
        GPIO.output(G2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(G1, GPIO.LOW)
        GPIO.output(G2, GPIO.LOW)
        GPIO.output(Y1, GPIO.HIGH)
        GPIO.output(Y2, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(Y1, GPIO.LOW)
        GPIO.output(Y2, GPIO.LOW)

def fastBlink(pin):
    """make one LED blink fast"""
    for i in range(0, 5):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.05)

def fastBlinkCycle():
    """cycle through all the LEDs and back, making each one blink fast """
    for pin in LEDS:
        fastBlink(pin)
    for pin in reversed(LEDS):
        fastBlink(pin)

def shutdownConfirm(junk1, junk2):
    """the initiate shutdown has been pressed"""
    global mode
    #allow time for other subroutine to finish flashing whatever LEDs it's flashing
    time.sleep(3)
    allon()
    time.sleep(0.5)
    
    #this is now in shutdown mode. The switch must be pressed to confirm this.
    mode = 77

    fastBlink(R2)
    GPIO.output(R1, GPIO.LOW)
    fastBlink(R2)
    GPIO.output(Y1, GPIO.LOW)
    fastBlink(R2)
    GPIO.output(G1, GPIO.LOW)
    fastBlink(R2)
    GPIO.output(B1, GPIO.LOW)
    fastBlink(R2)
    GPIO.output(B2, GPIO.LOW)
    fastBlink(R2)
    GPIO.output(G2, GPIO.LOW)
    fastBlink(R2)
    GPIO.output(Y2, GPIO.LOW)
    fastBlink(R2)
    GPIO.output(R2, GPIO.LOW)

    #the switch has not been pressed in time; cancel shutdown mode
    mode = 0

def modeSelect(channel):
    """
    Procedure:
        first click: start cycling through the patterns (this has to be done as a separate thread, 
                     so that the program can listen for another click)
        second click: if during the ripple, then stop the cycling and initiate shutdown confirm mode
        third click: if clicked during the confirm phase, then shutdown the computer.
        The confirm phase only lasts a few seconds until the lights go out one by one.
    """

    global mode
    if mode == 0:
        try:
            thread.start_new_thread(cyclePatterns,('MyStringHere',1))
        except Exception as errtxt:
            print errtxt

    #if clicked during ripple begin shutdown procedure
    if mode == 3:
        mode = 99
        try:
            thread.start_new_thread(shutdownConfirm,('MyStringHere',1))
        except Exception as errtxt:
            print errtxt

    if mode == 77:
        subprocess.call('sudo shutdown -h now', shell=True)
        #you can tell if the Raspberry Pi is shutdown because the switch no longer works (and you can't ping or ssh to it).


def cyclePatterns(junk1,junk2):
    """cycle through all patterns"""
    global mode
    MAXMODES = 6
    while (mode <= MAXMODES):
        if mode == 0:
            alloff()
        elif mode == 1:
            allon()
            time.sleep(1.0)
        elif mode == 2:
            altern(5)
        elif mode == 3:
            ripple(7)
        elif mode == 4:
            color(5)
        elif mode == 5:
            flash(5, LEDS)
        elif mode == 6:
            fastBlinkCycle()

        time.sleep(0.01)
        mode += 1
    #reset to starting value
    mode = 0

def main():
    setup()
    flash(5, LEDS[::2] )
    flash(5, LEDS[1::2] )
    try:
        while True:
            #    GPIO.wait_for_edge(SW1, GPIO.RISING)
            #    flash(5, LEDS)
            time.sleep(0.1)
            ###GPIO.wait_for_edge()
    except KeyboardInterrupt:
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
    GPIO.cleanup()


main()


#  global time_stamp       # put in to debounce
#     time_now = time.time()
#     if (time_now - time_stamp) >= 0.3:
#         print "Rising edge detected on port 24 - even though, in the main thread,"
#         print "we are still waiting for a falling edge - how cool?\n"
#     time_stamp = time_now
# ===================================================
# #!/usr/bin/python
#
# import thread
# import time
#
# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print "%s: %s" % ( threadName, time.ctime(time.time()) )
#
# # Create two threads as follows
# try:
#    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print "Error: unable to start thread"
## except Exception, e:
##    print str(e)#
# while 1:
#    pass


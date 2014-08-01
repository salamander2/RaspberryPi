#!/usr/bin/env python

#from lcd_display import lcd
import lcd_display
import RPi.GPIO as GPIO
from subprocess import *
from time import sleep, strftime
from datetime import datetime

#pin number for switch
SW1=11

mode=1

myLCD = lcd_display.lcd()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(SW1, GPIO.RISING, callback=changeMode, bouncetime=300)

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

IPCMD = "ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"
ipaddr = run_cmd(IPCMD).rstrip('\n')

WEATHCMD="wget -qO- http://wxdata.weather.com/wxdata/weather/local/CAXX0255?cc=*\&unit=m | grep tmp | sed 's/[^0-9]*//g'"
temper = run_cmd(WEATHCMD).rstrip('\n')

def changeMode(junk1):
    global mode
    mode = mode + 1
    if mode > 4:
        mode = 1
    myLCD.clear()

def main():
    setup()
    while 1:
        if mode == 1:
            myLCD.display_string("Welcome. Press",1)
            myLCD.display_string("btn to chng mode", 2)
        if mode == 2:            
            myLCD.display_string('IP %s' % ( ipaddr ),2)
        if mode == 3:            
            myLCD.display_string('Temp = %sC' % ( temper ),2)
        if mode == 4:
            myLCD.clear()
            time = datetime.now().strftime('%b %d %H:%M:%S')
            myLCD.display_string(time,1)

        sleep(2)

try:
    main()
except KeyboardInterrupt:
    myLCD.clear()
    GPIO.cleanup()
    myLCD.display_string("Bye!",1)


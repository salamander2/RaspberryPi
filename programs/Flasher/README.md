Flasher
=======

This is a Raspberry Pi program to flash LEDs in different patterns and also shutdown the Raspberry Pi (based on switch presses)

### 1. Here is a video of the flasher program running 
![Video](https://i1.ytimg.com/vi/eaOr0dMoI64/mqdefault.jpg) **[http://youtu.be/eaOr0dMoI64]   Have a look at it!**

*(Click the URL link not the image)*


### 2. Here are photos of the way I set up the GPIO breakout and the breadboard.


![Photo 1](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/Flasher/flasher1.jpg)
![Photo 2](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/Flasher/flasher2.jpg)
![Photo 3](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/Flasher/flasher3.jpg)

### 3. And here is the schematic:
![fritzing](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/Flasher/Flasher_bb.png)

-------

## 4.  Pulse program

* I've added a program called **"Pulse.py"** .  
  * This will make one red and one blue LED pulse. 
  * It's using PWM (pulse width modulation) to control the brightness of the LEDs.  
  * It uses the same setup (hardware layout) as the Flasher project
  * Just pick any two LEDs you want to pulse .
 
I got the code from [here](http://raspi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control). There's a video near the bottom of the page.

* I have simplified the code a bit for the workshop. That code is in my other repository.

------


#### 5. I changed rc.local so that my program starts when the RPi boots up.

```
~/myPython> $ cat /etc/rc.local
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

#run my Python flasher script on bootup (make sure that the path is correct)
sudo /home/pi/myPython/Flasher.py &

exit 0
```

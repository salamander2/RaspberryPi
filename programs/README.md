Various Raspberry Pi programs
=============================

I'm putting my various programs that I write here. I'll try and add photos too.

If they get to be big and complicated, I'll make a separate subfolder for them.  The FLASHER program is the first one that is in a separate folder.

----

### 1. Colour.py

**Photos**
![Circuit](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour_a.jpg)


![Part of circuit that is used for this project](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour_b.jpg)
I've left the circut for the Flasher program on the breadboard and just used another corner of it for the 3 colour LED.
I crossed out the White wire -- it's going to the switch for the Flasher circuit. You just need 3 resistors connecting from 3 GPIO pins to the three shorter legs of the LED. The long leg goes into the connector for the ground wire. Find out which leg controls which colour by trial and error (or look it up).

![Screen shot of program running](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour_c.jpg)

![another screen shot](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour_d.jpg)

The **Colour.py** program is used to control the colour of the tri-colour LED.
  * The shorter three legs connect to resistors which then connect to GPIO pins. You can see in the code where I set the pin numbers.
  * The long leg connects to ground. You can use a jumper wire to connect it. 
  * If you want a photo let me know.
  * I had some trouble getting Python to respond to a keypress. I found the code online -- it works nicely.
  * Pressing r, g, b makes the red, green and blue LEDs get brighter (up to 100%). Capital R, G, B make them dimmer down to 0%.  
  * Press "c" to quit (cancel the program).
  * For troubleshooting, I'm also printing out the rgb values. 
  * Note: for the keypresses to work, you'll have to connect via SSH (or HDMI and USB keyboard).

----

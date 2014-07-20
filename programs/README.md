Various Raspberry Pi programs
=============================

I'm putting my various programs that I write here. I'll try and add photos too.

If they get to be big and complicated, I'll make a separate subfolder for them.  The FLASHER program is the first one that is in a separate folder.

* The **Colour.py** program is used to control the colour of the tri-colour LED.
  * The shorter three legs connect to resistors which then connect to GPIO pins. You can see in the code where I set the pin numbers.
  * The long leg connects to ground. You can use a jumper wire to connect it. 
  * If you want a photo let me know.
  * I had some trouble getting Python to respond to a keypress. I found the code online -- it works nicely.
  * Pressing r, g, b makes the red, green and blue LEDs get brighter (up to 100%). Capital R, G, B make them dimmer down to 0%.  
  * Press "c" to quit (cancel the program).
  * For troubleshooting, I'm also printing out the rgb values. 
  * Note: for the keypresses to work, you'll have to connect via SSH (or HDMI and USB keyboard).

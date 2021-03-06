Three Colour LED program
========================

### Program name: TriColour.py

*You'll see below that the circuit is actually much simpler than it looks.*

**Photos**
![Circuit](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour/TriColour_a.jpg)

**>> Click here for my [YouTube Video](https://www.youtube.com/watch?v=ojwL1GuAkUk) of it in action. <<**

![Part of circuit that is used for this project](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour/TriColour_b.jpg)
I've left the circut for the Flasher program on the breadboard and just used another corner of it for the 3 colour LED.
I crossed out the White wire -- it's going to the switch for the Flasher circuit. You just need 3 resistors connecting from 3 GPIO pins to the three shorter legs of the LED. The long leg goes into the connector for the ground wire. Find out which leg controls which colour by trial and error (or look it up).

![Screen shot of program running](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour/TriColour_c.jpg)
Screen shot of program running

![another screen shot](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour/TriColour_d.jpg)
Another screen shot of the program running.

The **TriColour.py** program is used to control the colour of the tri-colour LED.
  * The shorter three legs connect to resistors which then connect to GPIO pins. You can see in the code where I set the pin numbers.
  * The long leg connects to ground. You can use a jumper wire to connect it. 
  * If you want a complete circuit diagram let me know.
  * I had some trouble getting Python to respond to a keypress. I found the code online -- it works nicely.
  * Pressing r, g, b makes the red, green and blue LEDs get brighter (up to 100%). Capital R, G, B make them dimmer down to 0%.  
  * Press "q" or "c" to quit (cancel the program).
  * For troubleshooting, I'm also printing out the rgb values. 
  * Note: for the keypresses to work, you'll have to connect via SSH (or HDMI and USB keyboard).

----
![Schematic diagram](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/TriColour/RGB_Colour_bb.png) This is a schematic diagram made by Fritzing. (www.fritzing.org)

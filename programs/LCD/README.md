LCD Display
===============================
### 1 Harware
I am using a 16x2 LCD panel. This is 16 characters in two rows, made up of dots (5x8 per character, not 7 segment LEDs).
On the back of it is something that I believe is called a backpack. It says YwRobot Arduino LCM1 602 IIC VI.
This is the part that I plug my four wires into to get it working. See the last photo on this page for more details.

### 2. Configuring Linux
Yes, this is **not** just plug and play. You have to do a bit of work, but not too much because I've written all the steps here for you (from http://skpang.co.uk/blog/archives/575).

1. `sudo nano /etc/modprobe.d/raspi-blacklist.conf`
then add a # to comment out i2c-bcm2708

2. `sudo nano /etc/modules`
add i2c-dev to a new line.

3. then type these commands to install the software you need
`sudo apt-get update` , `sudo apt-get install i2c-tools` , `sudo apt-get install python-smbus`

4. finally ...  `sudo adduser pi i2c`  and `sudo shutdown -r now`

5. plug in the i2c hardware

6. test it with the following command: `sudo i2cdetect -y 1` 
You should see something like this which tells you the address of your i2c hardware.

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- UU -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --  
```

Here it tells me that my I2C address is **27**. If this doesn't work (you don't see anything), then reboot again AFTER you've plugged in the hardware.

### 3 Programs
You need to copy the 3 programs all into the same folder on your Raspberry Pi: 
* **LCDtext.py** This is the program that I wrote to do stuff
* **lcd_display.py** This program creates the LCD object in python and provides methods for using it.
* **i2c_lib.py** This is an I2C library that does the interfacing with the LCD screen over the I2C pins.
* The above two programs were from the repository https://github.com/paulbarber/raspi-gpio
Note that this software does not require that Quick2Wire or any other extra stuff be installed.

*There is extra stuff that you can do, like making your own characters, etc. But I don't know how to do it yet.  I can't even get the cursor to show up and flash.*

### 4 Photos
![photo1](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_1.jpg)

![photo2](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_2.jpg)

This will change what is displayed each time I push the button.

![photo3](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_3.jpg)

Here it is displaying my IP address (which it gets from running a Linux (bash) script).

![photo4](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_4.jpg)

This is displaying the temperature from the local weather report.  Again, this is from a linux script, I don't yet have a thermometer hooked up.

![photo5](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_5.jpg)

Here is the current date and time, updated every two seconds.

![photo6](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_6.jpg)
And this is the back of the LCD panel. On the YwRobot thing, the red LED shows that it has power. The blue square is a variable resistor which can be turned with a screwdriver to change the contrast. And finally, the two pins on the left normally have a jumper which enables the backlight. It was just too bright for my camera (see the first one for example). You can see the four pins on the right that connect to the breadboard. GND is ground, VCC is +5V, the other two SDA and SCL connect to the GPIO SDA and SCL pins.

### 5 Schematic
![schematic](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_bb.png) This diagram (made using Fritzing) doesn't show the connectors on the back of the LCD display, so I show the wires connected on the side of it.  Again, the ribbon cable is not shown.
It is very important to make sure that the correct wires go into the correct pins. The four wires are **not** interchangeable.


LCD Display
===============================
### 1 Harware
I am using a 16x2 LCD panel. This is 16 characters in two rows, made up of dots (not 7 segment LEDs).
On the back of it is something that I believe is called a backpack. It says YwRobot Arduino LCM1 602 IIC VI.
This is the part that I plug my four wires into to get it working.

### 2 Programs
You need to copy the 3 programs all into the same folder on your Raspberry Pi: 
* **LCDtext.py** This is the program that I wrote to do stuff
    * 
* **lcd_display.py** This program creates the LCD object in python and provides methods for using it.
* **i2c_lib.py** This is an I2C library that does the interfacing with the LCD screen over the I2C pins.
* The above two programs were from the repository https://github.com/paulbarber/raspi-gpio
Note that this software does not require that Quick2Wire or any other extra stuff be installed.

### 3 Photos
![photo1](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_1.jpg)

![photo2](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_2.jpg)
![photo3](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_3.jpg)
![photo4](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_4.jpg)
![photo5](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_5.jpg)
![photo6](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_6.jpg)

### 4 Schematic
![schematic](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_bb.png) This diagram (made using Fritzing) doesn't show the connectors on the back of the LCD display, so I show the wires connected on the side of it.  Again, the ribbon cable is not shown.
It is very important to make sure that the correct wires go into the correct pins. The four wires are **not** interchangeable.


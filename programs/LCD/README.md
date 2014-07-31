LCD Display
===============================
### 1 Harware

### 2 Programs
You need to copy the 3 programs all into the same folder on your Raspberry Pi: 
* **LCDtext.py** This is the program that I wrote to do stuff
    * 
* **lcd_display.py** This program creates the LCD object in python and provides methods for using it.
* **i2c_lib.py** This is an I2C library that does the interfacing with the LCD screen over the I2C pins.
* The above two programs were from the repository https://github.com/paulbarber/raspi-gpio
Note that this software does not require that Quick2Wire or any other extra stuff be installed.

### 3 Photos

### 4 Schematic
![schematic](https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/LCD/LCD_bb.png) This diagram (made using Fritzing) doesn't show the connectors on the back of the LCD display, so I show the wires connected on the side of it.  Again, the ribbon cable is not shown.
It is very important to make sure that the correct wires go into the correct pins. The four wires are **not** interchangeable.


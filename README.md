Raspberry Pi programs and setup
===============================

### 1 How to set up your Raspberry Pi
[from James Doyle's Raspberry Pi course](https://github.com/james2doyle/raspberry-pi-course)


#### Install Rasbian

* download [NOOBs offline](http://www.raspberrypi.org/downloads/) and unzip it onto the SD Card you want to use
* Choose the Rasbian option by hitting the `spacebar` and then press `i` to start the installation
* make sure your keyboard is **US and not GB**
* the default username and password is  "pi" and "raspberry", respectively
* once installed the system will reboot
* login with the default credentials
* you are now logged into the shell. Use `startx` to launch the desktop

#### Keyboard Problems

If you press the `~` key and see that it is not `~` that means your keyboard is not setup properly.

* run `sudo raspi-config` from the command line
* highlight `4 Internationalisation Options` and press enter
* you should see an option for keyboard layout, select that
* you should change to a `Generic Key` keyboard when in doubt
* the next pages will let you set a locale for the keyboard, we want US not UK
* Choose other in the language choice
* Choose US for the next choice
* you can leave everything else default and just press enter throughout

#### Setup WiFi

* Run `sudo nano /etc/network/interfaces` to open the network config
* Ignore the stuff about the `eth0` device. Change the stuff about `wlan0` to the following, delete things if necessary.

```
auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
auto wlan0

iface wlan0 inet dhcp
        wpa-ssid "networkname"
        wpa-psk "password"
```

* save the file with `ctrl+o`, confirm the filename with `y`, and press `ctrl+x` to close nano.
* restart the RPi with `sudo shutdown -r now`

#### Update

* Update the list of packages (repositories) with `sudo apt-get update`
* Upgrade the RPi with `sudo apt-get upgrade`
* You should do this every month or so to apply the most recent patches to the operating system.

#### Installing the required tools

* Install `git`
  * run `sudo apt-get install git`
  * accept the dependencies with `y`
  * check that git is installed with `which git`, a path should be returned


### 2 Programs
NOTE: The main program right now is "Flasher" -- have a look under programs/Flasher

### 3 Some references for GPIO pins
 
 * GPIO P1 Header Pinouts: http://elinux.org/Rpi_Low-level_peripherals#P1_header
 
 * More details for pinouts: http://elinux.org/RPi_BCM2835_GPIOs


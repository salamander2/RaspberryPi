Raspberry Pi programs and setup
===============================

### 1 How to set up your Raspberry Pi
[(from James Doyle's Raspberry Pi course)](https://github.com/james2doyle/raspberry-pi-course)


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

#### Useful Linux Commands

Most of these commands have options and/or take parameters. e.g. `ls -la *py`
* sudo : this is "superuser do". Linux prevents you from really screwing up the operating system by not letting you mess with important files. If you really really want to do this, you have to be a superuser (and "pi" is), and then prefix your command with the word `sudo`.
* nano : this is a simple editor.  The two main Linux editors are vi and emacs. Both are hideously complicated (but fun).
* ls : list files. There are many options to the `ls` command.  `ls -l`  and `ls -a` are two I use a lot
* cat : this displays a file (prints it to the screen)  e.g. `cat /etc/rc.local`
* pwd : display present working directory
* cd : change directory
* man : look un the manual (man page) for something. e.g. `man python`
* apt-get : this is the main (best??) way to install new software. e.g. `sudo apt-get install git`   Other useful options are `sudo apt-get autoremove` . It also updates your software and patches it.
* 

Command line: 
* use the up and down arrow keys to see previous commands
* to search for a command, type CTRL-R and then any text in the command. You can either keep typing in more text, or use CTRL-R again to go through all of the possibilities.  e.g. look for a previous command that has "re" in it.
* command completion/searching. You can find commands that are on the path, by typing the first part of the command and then hitting TAB twice. e.g. List all the commands that start with "smb", type `smb<tab><tab>`
* history : type this to get a list of all of the commands you've typed. (It only saves the most recent 1000. To save more, edit the file ".bashrc"). If you only want to see the past 50 commands, type `history | tail -50`.  If you want to page through them all type `history | less` or `history | more`

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

#### Update Linux

* Update the list of packages (repositories) with `sudo apt-get update`
* Upgrade the RPi with `sudo apt-get upgrade`
* You can combine this into one command: `sudo apt-get update && sudo apt-get upgrade`
* You should do this every month or so to apply the most recent patches to the operating system.

#### Installing the required tools

HOW TO USE GIT ...

* Install `git`
  * run `sudo apt-get install git`
  * accept the dependencies with `y`
  * check that git is installed with `which git`, a path should be returned


### 2 Programs
NOTE: The main program right now is "Flasher" -- have a look under programs/Flasher

### 3 Some references for GPIO pins
 
 * GPIO P1 Header Pinouts: http://elinux.org/Rpi_Low-level_peripherals#P1_header
 
 * More details for pinouts: http://elinux.org/RPi_BCM2835_GPIOs


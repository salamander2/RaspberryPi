### GUI desktop commands
Once you have run `startx` to start the desktop windows, if you have no mouse plugged in, use these:
* ALT-F2 will pop up a box where you can type in the program you want to run
* CTRL-ESC will bring up the main menu
* SHIFT-F10 is the same as right-clicking the mouse buttons
* To exit the GUI and go back to the command prompt, logout using the option at the bottom of the start menu.

#### Useful Linux Commands (for the command line):
All linux commands are lower case (as far as I know). File names (and everything else) is case sensitive.

Most of these commands have options and/or take parameters. e.g. `ls -la *py`
* **sudo** : this is "superuser do". Linux prevents you from really screwing up the operating system by not letting you mess with important files. If you really really want to do this, you have to be a superuser (and "pi" is), and then prefix your command with the word `sudo`.
* **nano** : this is a simple editor.  The two main Linux editors are vi and emacs. Both are hideously complicated (but fun).
* **ls** : list files. There are many options to the `ls` command.  `ls -l`  and `ls -a` are two I use a lot
* **cat** : this displays a file (prints it to the screen)  e.g. `cat /etc/rc.local`
* **date** : this displays the current date and time
* **pwd** : display present working directory
* **cd** : change directory.  
    * You can also always get to the home directory by typing `cd`
    * `cd -` will take you to the previous directory you were in
    * You can get to a complicated location (eg. ./quick2wire_some_stuff) by typing just the first few letters and then pressing tab. `cd qui<TAB>`
* **mkdir** : make a sub directory
* **rm** ... : delete (remove) files or directories.
   * If it's an empty directory, use **rmdir**
* **man** : look un the manual (man page) for something. e.g. `man python`
* **apt-get** : this is the main (best??) way to install new software. e.g. `sudo apt-get install git`   
Other useful options are `sudo apt-get autoremove` . "apt-get" is the command that also updates your software and patches it.
* **df** : how much disk free space you have. `df -h` is better
* **passwd** : this is the command to change your password
* **ifconfig** : information about all network devices
* **iwconfig** : information about all WiFi network devices (different info from ifconfig)
* **shutdown** : this is how you shutdown and restart/power off the RPi. Read the man pages for options (normally just `sudo shutdown -r now`). Must be run using sudo.
* **exit** : This is how you log off of any linux command line session. It will log you out of an SSH connection too.
* How to tell what version of Linux you are running: (All of these give slightly different information.)
   * **uname -a**
   * **lsb_release -a**
   * **cat /etc/issue**
   * **cat /etc/os-release** 
* **cat /proc/cpuinfo** will tell you what CPU your computer has.
* **touch /forcefsck** : force a drive check on next reboot 

### Using Command line: 
* use the up and down arrow keys to see previous commands
* to search for a command, type CTRL-R and then any text in the command. You can either keep typing in more text, or use CTRL-R again to go through all of the possibilities.  e.g. look for a previous command that has "re" in it.
* command completion/searching. You can find commands that are on the path, by typing the first part of the command and then hitting TAB twice. e.g. List all the commands that start with "smb", type `smb<tab><tab>`
* **history** : type this to get a list of all of the commands you've typed. (It only saves the most recent 1000. To save more, edit the file ".bashrc"). If you only want to see the past 50 commands, type `history | tail -50`.  If you want to page through them all type `history | less` or `history | more` 

====

## How to copy/backup Raspberry Pi SD card.
This assumes that you are using a Linux computer _(so it's mostly a handy reference for me!)_
:x: This must be to the same size SD card, and probably the same manufacturer too. :bangbang:

1. Find where the SD card is located. Normally it is at **/dev/sdb** , so this is what I'm using in this example. Make sure that it is not mounted `df -h`
2. Change to the directory where you want to store the backups (e.g. on a USB drive or /home/yourname/RPI_backup )
3. backup MBR: `sudo dd if=/dev/sdb of=backup-sdb.mbr count=1 bs=512`
4. backup extended partitions: `sudo sfdisk -d /dev/sdb > backup-sdb.ext`
5. copy all data: `sudo dd if=/dev/sdb of=backup-sdb.dd bs=1M`  **make sure that there is enough space on the USB drive first!**

### How to restore the data to another SD card:
0. Change to the directory where the backups are stored.
1. Restore MBR: `sudo dd if=backup-sdb.mbr of=/dev/sdb`
2. restore extended partitions: `sudo sfdisk /dev/sdb < backup-sdb.ext`
3. restore all data: `sudo dd if=backup-sdb.dd of=/dev/sdb bs=1M`

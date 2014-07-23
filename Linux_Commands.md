### GUI desktop commands
Once you have run `startx` to start the desktop windows, if you have no mouse plugged in, use these:
* ALT-F2 will pop up a box where you can type in the program you want to run
* CTRL-ESC will bring up the main menu
* SHIFT-F10 is the same as right-clicking the mouse buttons
* ALT-F1 does something

#### Useful Linux Commands (for the command line):

Most of these commands have options and/or take parameters. e.g. `ls -la *py`
* sudo : this is "superuser do". Linux prevents you from really screwing up the operating system by not letting you mess with important files. If you really really want to do this, you have to be a superuser (and "pi" is), and then prefix your command with the word `sudo`.
* nano : this is a simple editor.  The two main Linux editors are vi and emacs. Both are hideously complicated (but fun).
* ls : list files. There are many options to the `ls` command.  `ls -l`  and `ls -a` are two I use a lot
* cat : this displays a file (prints it to the screen)  e.g. `cat /etc/rc.local`
* pwd : display present working directory
* cd : change directory.  
    * You can also always get to the home directory by typing `cd`
    * `cd -` will take you to the previous directory you were in
    * You can get to a complicated location (eg. ./quick2wire_some_stuff) by typing just the first few letters and then pressing tab. `cd qui<TAB>`
* man : look un the manual (man page) for something. e.g. `man python`
* apt-get : this is the main (best??) way to install new software. e.g. `sudo apt-get install git`   Other useful options are `sudo apt-get autoremove` . It also updates your software and patches it.
* df : how much disk free space you have. `df -h` is better


### Using Command line: 
* use the up and down arrow keys to see previous commands
* to search for a command, type CTRL-R and then any text in the command. You can either keep typing in more text, or use CTRL-R again to go through all of the possibilities.  e.g. look for a previous command that has "re" in it.
* command completion/searching. You can find commands that are on the path, by typing the first part of the command and then hitting TAB twice. e.g. List all the commands that start with "smb", type `smb<tab><tab>`
* history : type this to get a list of all of the commands you've typed. (It only saves the most recent 1000. To save more, edit the file ".bashrc"). If you only want to see the past 50 commands, type `history | tail -50`.  If you want to page through them all type `history | less` or `history | more`

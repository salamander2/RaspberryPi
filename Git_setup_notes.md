My notes on how to set up Git to connect with Git Hub
============

(I'm doing this on a Raspberry Pi)

Clone my RaspberryPi project. This will make a _copy of the whole git repository_ and store it in a folder called RaspberryPi. It copies the programs, readme files, images, etc. 
* `cd`  go to home directory
* `git clone https://github.com/salamander2/RaspberryPi`  

How to _get one file_ and save it in the current directory :
`wget https://raw.githubusercontent.com/salamander2/RaspberryPi/master/programs/Flasher/Flasher.py`

-----

### How to actually use Git to track and store programs

####1. Set up GitHub account
You need to have a GitHub account set up.  This implies that you need an email address too.
Make a repository on GitHub.  e.g. I made one called RaspberryPi

####2. If git is not installed, install it. 

Git is already installed with Raspbian. If it wasn't installed and you needed to install it, you would do the following:
  * run `sudo apt-get install git`
  * accept the dependencies with `y`
  * check that git is installed with `which git`, a path should be returned


####3. Set up the main parts of Git
```
git config --global user.name "salamander2"
git config --global user.email "salamander2@email.com"
```

####4. Make a public/private key

```
    ssh-keygen -t rsa -C "salamander2@email.com"

    Generating public/private rsa key pair.
    (type in a passphrase here)
    
    Your identification has been saved in /home/pi/.ssh/id_rsa.
    Your public key has been saved in /home/pi/.ssh/id_rsa.pub.
    The key fingerprint is:
    6a:11:22:33:44:xx:yy:zz:blahblahblah salamander2@email.com
    The key's randomart image is:
    +--[ RSA 2048]----+
    | .  . .          |
    |o  . . +         |
    ...
    |.o   .           |
    |x .              |
    +-----------------+
```

#####5. Copy this public key to github

* In your github.com account, go to account settings
* click on SSH keys
* click on add SSH key
* on your raspberry pi, `cat ~/.ssh/id_rsa.pub`
* copy the output of this command (the contents of the id_rsa.pub file) and paste it into the appropriate place in the GitHub screen.

####6. Now test the connection to GitHub to make sure that it works.

On your Raspberry Pi, type the following
```
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa
              #You'll have to type in your passphrase here when asked
ssh -T git@github.com
```

You may see something like this:
```
The authenticity of host 'github.com (192.30.252.131)' can't be established.
RSA key fingerprint is 16:27:ac:xx:xx:xx:xx:xx:.....
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.252.131' (RSA) to the list of known hosts.
Hi salamander2! You've successfully authenticated, but GitHub does not provide shell access.

```

##Using Git

**Important:** change to the directory that will be a mirror of your GitHub repository
(i.e. `mkdir myPython`  then `cd myPython`)
Now we'll set up this directory to be a mirror of the RaspberryPi repository on GitHub
```
git init
git remote add origin ssh://git@github.com/salamander2/RaspberryPi
git remote set-url origin git@github.com:salamander2/RaspberryPi

git remote -v     #just testing. The following two lines are displayed
    origin	git@github.com:salamander2/RaspberryPi (fetch)
    origin	git@github.com:salamander2/RaspberryPi (push)

```

#### *I'm not an expert on Git, so I basically just use the following commands in this order*
There are many good references on the internet. e.g. http://git-scm.com/book/en/Git-Basics-Recording-Changes-to-the-Repository
Note: if you want to make a subfolder, you have to also put at least on file in it.

#### Add 
`git add *`

This command will add any files in the directory to the list to be mirrored with the repository. Any time you create a new file locally, you have to add it.

#### Pull
`git pull origin master`

This command will get the lastest versions of all of the files on the github repository. Normally this is the first thing you do.  If you have modified files on your Raspberry Pi more recently than the ones on GitHub, it will not overwrite them. 

#### Status
`git status -s`

This command is used to check the status of the added files.


#### Commit
`git commit -am 'updated comments'`

This commits your changes (whatever that means!). You have to add a message to say what your changes are.

#### Synchronize:
`git push origin master`

Send your changed files to the GitHub repository. Note, it seems that `git pull origin master` also sometimes sends your updated files to GitHub

#### Deleting files
`git add -A *`

This will automatically track files that have been deleted (locally) and delete them on GitHub (after a commit and push).  Another possible method is `git rm $(git ls-files --deleted) `

#### Recovering past versions
When I accidentally delete something or need to go back to a previous version, I'll figure this part out.

I think I do something like this (in the same folder as the messed up file, in this case Flasher.py) `git checkout -- Flasher.py`


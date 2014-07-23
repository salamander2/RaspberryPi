My Notes on how to set up Git to connect with Git Hub
============

I'm doing this on a Raspberry Pi

####1. Set up GitHub account
You need to have a GitHub account set up.  This implies that you need an email address too.
Make a repository on GitHub.  e.g. I made one called RaspberryPi

####2. If git is not installed, install it. 
 
`sudo apt-get install git`

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

git remote -v     #just testing
```

#### Add 
`git add *`

This command will add any files in the directory to the list to be mirrored with the repository. Any time you create a new file locally, you have to add it.

#### Pull
`git pull origin master`

This command will get the lastest versions of all of the files on the github repository. Normally this is the first thing you do.

#### Status
`git status -s`

This command is used to check the status of the added files.


#### Commit
`git commit`  or `git commit -m 'updated comments'`

This commits your changes (whatever that means!). You have to add a message to say what your changes are.

#### Synchronize:
`git push origin master`

Send your changed files to the GitHub repository. Note, it seems that `git pull origin master` also sometimes sends your updated files to GitHub





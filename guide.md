Security
---------

Ask for a second opinion from a moderator before operating any code with these imports:

    import os         # operating system interface
    import sys        # provides access to variables used by the interpreter 
    import socket     # low level networking interface (probably will never be used in a bot)
    import subprocess # allows the script to spawn new processes

While they do have legitimate uses, you should know why they are in the bot.

Don't download any scripts that have been converted to .exe files via something like [py2exe](http://www.py2exe.org/). Always ask for the .py file if it is not given to you.

Don't download Python from any source except for python.org or your OS's package manager, and don't install any modules that your script may require from anything except `pip` (instructions for both are listed below). If the module your script requires is not available via `pip` then only download it from a reputable source (i.e. github).

If you have any concerns at all, ask. Ask the person that made it, or mention me or any of the mods, and we'd be happy to look over the code to make sure none of it is malicious and will be okay.

The instructions listed for setup below will get 99% of bots working, if your bot maker asks you to install or do anything else ask why!

-----------------------------------------------------------------------------------------------------------------------------------

Setup (Windows)
-------------------

First thing you will need to do, is install python if you don't already have it installed.
There are two common versions of python currently in use. Python 2 and Python 3. Which one 
you'll need entirely depends on which version your bot is written for. If you're unsure, just
ask the creator and they'll be more than happy to tell you.

[Go here to download the latest releases of Python](https://www.python.org/downloads/windows/)

After you click the latest version you need, you'll want to download the `Windows x86-64 MSI installer` and run it.

Great, you're halfway to being able to run your bots!

Next thing you will need is to install some packages for Python to make 
the bot work. As it stands right now, if you try running you'll get quite a few errors.
That's where `pip` python's friendly package manager comes in. And luckily with the latest
versions of Python it comes installed with it. So now what you should do is open up 
powershell, by going to run and typing in powershell, or searching for it on Win8.

Then you'll want to type in the command to install the package like so:

    py -m pip install {package} # python 2
    py -3 -m pip install {package} # python 3

Praw will be one you will have to install as it's the the package for python to access
Reddit's API. Some other common ones will be BeautifulSoup(parses web pages) and OAuth2-Util
(handles reddit's authorization). To install all 3 (only install the last two if you have to):

    # Python 2
    py -m pip install praw
    py -m pip install praw-oauth2util # only if your script requires it
    py -m pip install beautifulsoup4 # only if your script requires it
    # Python 3
    py -3 -m pip install praw
    py -3 -m pip install praw-oauth2util # only if your script requires it
    py -3 -m pip install beautifulsoup4 # only if your script requires it

[Python 2 pip install screenshot](http://i.imgur.com/Yvfl0Mj.png)

[Python 3 pip install screenshot](http://i.imgur.com/79Kr3cm.png)

If you get an error along the lines of 

    the term 'python'/'py' is not recognized as the name of a cmdlet, function, script file, or operable program`

 Try typing this into power shell which will point powershell to python when they command is typed in: 

    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User") # python 2
    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python34", "User") # python 3

If that still gives you errors try setting the path with this:

     $env:path="$env:Path;C:\Python27 # python 2
     $env:path="$env:Path;C:\Python34 # python 3

If neither of those get it working, leave a comment, I'm trying to make sure I get all the bases covered with Windows to make this as easy as possible for people to setup!

And there you go, they are all installed! If you have any errors installing these with pip, 
[see this StackOverflow post with fixes for common issues](http://stackoverflow.com/a/12476379/2826911).
And if that doesn't help, don't be afraid to ask somebody for help!

Now you are ready to run your bot. From here you have two options, running it from powershell/cmd, or from IDLE.

To run from powershell/cmd type in these commands:

    cd C:/Path/To/.py/File # i.e if on Desktop this would be cd C:/Desktop
    py bot_file.py # this will run python 2
    py -3 bot_file.py # this will run python 3

[Screenshot of powershell](http://i.imgur.com/eOv1hcQ.png).

And it should be running!

To run from IDLE, either find IDLE from your program menu or search for it. IDLE is python's interpreter.
Then go to file -> open and find your bot_file.py and open it. Then select Run -> Run Module (or press F5).
And it'll start running. And there you go, you're running a Reddit bot!

Setup (OS X/Linux)
------------------

If you're on Linux chances are python2 is already installed, but if you need python3 just open up terminal
and type (depending on your package manager):

    sudo apt-get python3 # or
    yum install python3

If you're on OS X you can either install by going to [Python's website and getting the latest releases](https://www.python.org/downloads/mac-osx/),
or (my personal recommendation) download [Homebrew package manager](http://brew.sh/). If you choose the Homebrew route, after installation
open terminal and type:

    brew install python # for python 2
    brew install python3 # for python 3

From there you will need to install the packages required for your bot to run. The one package you will need is praw. Some other common ones will be 
BeautifulSoup(parses web pages) and OAuth2-Util (handles reddit's authorization). Open terminal and type the commands:

    pip install {package}

For the common ones, these commands would be:

    pip install praw
    pip install praw-oauth2util # only required if you need them
    pip install beautifulsoup4 # only required if you need them

And now you're ready to run your bot! To do that open up your terminal and type:

    cd /Path/To/.py/File
    python bot_file.py # if it uses python2
    python3 bot_file.py # if it uses python3

[Screenshot example](http://i.imgur.com/92DyoJO.png).

Now your bot is running!

----------------------------------------------------------------------------------------------------------------------------------

Scheduling
----------

So you have a bot that needs to be run on a certain day/week/hour/etc. This is how you'll do that.

If you're on Windows, you'll want to use Task Scheduler.

* Open Task Scheduler and create a new task.
* [Give it a name and description if you want](http://i.imgur.com/fUHLizJ.png).
* [Create a trigger, and set it up for when you want it to run](http://i.imgur.com/d2wimY0.png)
* Then create a new action.
  * Set the Program/Script to either C:\Python27\python.exe or C:\Python34\python.exe
      * [For python 2](http://i.imgur.com/BkzsgTg.png)
      * [For python 3](http://i.imgur.com/lR9fN5z.png)
  * Set add arguments to the name of your .py file
  * Set the start in to the location of the .py file (ex. C:\Desktop)
* And then create the task.

[More information can be found here](http://blogs.esri.com/esri/arcgis/2013/07/30/scheduling-a-scrip/)

-----------------------------------------------------------------------------

If you're on OS X/Linux you'll want to use crontab. So open up your terminal and type:

    crontab -e

And it will ask you what editor you want to use if it's your first time. If you're unfamilar with
terminal text editors, choose Nano (or pick vi if you want to learn something or are a masochist).

The quick and dirty guide to Nano. Use your arrow keys to move the cursor. Go to the bottom and add your cronjob in the format listed below. And press `control + x` to exit and when asked press `y` to save it.

The format of all cronjobs will be:

    *     *    *   *   *        command to be executed
    -     -     -   -    -
    |     |     |   |    |
    |     |     |   |    +----- day of week (0 - 6) (Sunday=0)
    |     |     |   +------- month (1 - 12)
    |     |     +--------- day of month (1 - 31)
    |     +----------- hour (0 - 23)
    +------------- min (0 - 59)

So add a line for your script edit the stars to fit what kind of schedule you need it to run on.
Examples:

    # Runs at 1:45PM everyday
    45 13 * * * python /path/to/bot_file.py

    # Runs every 5 minutes
    */5 * * * * python /path/to/bot_file.py

    # Run on the 15th of February
    * * 15 2 * python /path/to/bot_file.py

    # Run on every Tuesday at 2:15PM
    15 14 * * 2 python /path/to/bot_file.py

[Screenshot of one of my cronfiles](http://i.imgur.com/bPEPB1O.png).

[More information on crontab can be found here](http://www.adminschoice.com/crontab-quick-reference)

And that's it!

----------------------------------------------------------------------------------------------------------------------------------

OAuth
-------

Reddit is deprecating password logins via it's API soon. Therefore you will no longer be able to just use your username and password to login your bot. You will have to use a app_key and app_secret. Every bot that uses OAuth will require both items, however the implementation may be different depending on who writes it and how they implement OAuth. So, you will have to get some direction from them on where they want these two things to go.

As for getting these items you will want to follow these steps:

* [Go here on the account you want the bot to run on](https://www.reddit.com/prefs/apps/)
* Click on create a new app.
* Give it a name. 
* Select script from the radio buttons.
* The redirect uri may be different, but will probably be `http://127.0.0.1:65010/authorize_callback`
* After you create it you will be able to access the app key and secret.
* The app key is found [here](http://i.imgur.com/7ybI5Fo.png) (**Do not give out to anybody**) (*I deleted this app after the screenshot*)
* And the app secret [here](http://i.imgur.com/KkPE3EV.png) (**Do not give out to anybody**)

And that's all you'll need. You'll authorize the bot on it's first run and you'll be good to go!

-----------------------------------------------------------------------------------------------------------------------------------

Other Reddit Things
----------------------

If you plan on creating a new account for your bot, keep in mind the bot has to have 10 link karma before it can post without you having to solve captcha, which defeats the purpose of having a bot, because you don't want to have to do it right? Well check out subs like /r/freekarma and post a picture of something to get that sweet karma. And if you post there, please upvote other posts so new users/bots can get some karma too!

Please don't use your bot to post harass/annoy/etc other users. Read the rules in the sidebar, nobody here will make a bot that does those things. There are exceptions to the rules if it's for a sub you moderate.

-----------------------------------------------------------------------------------------------------------------------------------

If you have any questions ask the person that made your bot or me. I'm always more than willing to help.

And if you make bots or just knowledgeable about running them and see something wrong, let me know and I'll fix it
and it's very late, so good chance I've messed something up (and I don't use Windows that often so there's probably some little errors in there).

Cheers!

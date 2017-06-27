# Getting Started
#### Here are the basic setup steps required to run your bot.
---
### 1 - Install Python 3
  - [Python 3.5](https://www.python.org/downloads/) or higher is recommended
  
### 2 - Install PRAW
  - Detailed installation instructions found [here](https://praw.readthedocs.io/en/latest/getting_started/installation.html)
  - Or simply execute this command in a terminal
    ```
    pip install praw
    ```
    
### 3 - Save the code
  - Your bot should be saved in a directory/folder by itself
  - Use the same names for the files as you find them here
  - Python files should be given `.py` as the file extension
  - Your bot will likely need a `.ini` file which contains your authorization credentials (Step 4)
  
### 4 - Authorize the bot
  - Sign in to [reddit](http://www.reddit.com) with the account you will use the bot with
  - Go to [https://www.reddit.com/prefs/apps/](https://www.reddit.com/prefs/apps/)
  - Click "Create an App"
  - Name the app
  - Select the bubble option for "script"
  - Put this uri into redirect uri: `http://www.example.com/unused/redirect/uri`
  - Click "Create App"
  - Record the hash string in the top left corner under "personal use script". This is your Client ID. Also record the "Secret." You will need these later to authenticate with Reddit
  - Go to the [Reddit API Access page](https://www.reddit.com/wiki/api) and click "Read the full API terms and sign up for usage."
  - Fill all required fields on the form and click submit
  
### 5 - Insert bot credentials
  - Create a file called `praw.ini` in the same directory as your bot
  - Enter the client_id and client_secret which you were given when creating your bot app. You can access those values [here](https://www.reddit.com/prefs/apps/)
  - Create a user_agent string following this format: 
    `Operating_System:Bot_Name:Version (by /u/Your_Username)`
  - Here is an example user_agent string:
    `Linux:Yes_Bot:0.1 (by /u/spez)`
  - [Here](https://github.com/kimpeek/reddit_bots/blob/master/templates/praw.ini) is an example `praw.ini` file
    
### 6 - Schedule the bot
  - Linux and Mac use [Crontab](http://www.linuxweblog.com/crotab-tutorial)
    - To run at startup, use `@reboot my_bot.py` and replace `my_bot` with the name of your script
  - Windows use [Task Scheduler](https://technet.microsoft.com/en-us/library/cc748993(v=ws.11).aspx)

---
#### Please see [this reddit post](https://www.reddit.com/r/RequestABot/comments/3d3iss/a_comprehensive_guide_to_running_your_bot_that/) for more detailed instructions if you are having difficulty.
---

## Resources

  - [Reddit API](https://github.com/reddit/reddit/wiki/API)
  - Praw [Documentation](https://praw.readthedocs.io/en/latest/index.html)
  - Praw [Source](https://github.com/praw-dev/praw)
  - Python [Documentation](https://docs.python.org/3/)
  - [/r/RequestABot](https://www.reddit.com/r/RequestABot/)
  - [/r/learnpython](https://www.reddit.com/r/learnpython/)
  - [Freenode IRC](http://webchat.freenode.net/?channels=%23%23learnpython)

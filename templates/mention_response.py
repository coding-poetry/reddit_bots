from time import sleep
import praw

reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    password='password',
    user_agent='user_agent',
    username='username'
)

response = """
Some Text Here
[Link]( Here )
___
^^I ^^am ^^a ^^bot.
"""


def main():
    """Check the inbox for mentions once every 30 seconds.
    Reply to all mentions with the response.
    Avoids duplicated responses by marking them as read"""

    while True:
        for mention in reddit.inbox.mentions():
            if mention.new:
                mention.reply(response)
                mention.mark_read()
        sleep(180)

if __name__ == '__main__':
    main()

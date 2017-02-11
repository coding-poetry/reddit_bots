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
    for mention in reddit.inbox.mentions():
        if mention.new:
            mention.reply(response)
            mention.mark_read()

if __name__ == '__main__':
    main()


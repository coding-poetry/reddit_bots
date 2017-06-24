import praw

reddit = praw.Reddit('AUTHENTICATION')
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


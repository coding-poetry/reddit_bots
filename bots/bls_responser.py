import praw

reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    password='password',
    user_agent='Windows/Linux:BLSbot:0.1 (by /u/user)',
    username='BLSbot'
)

response = """
[Here](https://www.bls.gov/cps/cpsaat39.htm) are the Bureau of Labor and Statistics data regarding median weekly earnings of full-time wage and salary workers by detailed occupation and sex.
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

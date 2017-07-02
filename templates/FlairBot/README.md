# FlairBot

### Remove unflaired posts after a period of time.

---

This bot can be used in conjunction with [/u/Automoderator](https://www.reddit.com/u/Automoderator) or without.
If used with [/u/Automoderator](https://www.reddit.com/u/Automoderator), you need to put the rule below into your config file located at 
[https://www.reddit.com/r/SUBREDDIT/wiki/config/automoderator](https://www.reddit.com/r/SUBREDDIT/wiki/config/automoderator).

You must also create a flair class of `Unflaired` for [/u/Automoderator](https://www.reddit.com/u/Automoderator) to apply.
FlairBot will look for this flair. If it is found on any posts older than the amount of time you set, the post will be removed.

```yaml
---
type: submission
set_flair: flair_css_class

comment: |
    Please remember to flair your submission within 10 minutes.

    Failure to apply a flair will result in your submission being removed.
```

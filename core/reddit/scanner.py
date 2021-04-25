import praw
import os
import sys
import reddit
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def sub_scan(r):
    subreddit = r.subreddit(config.WATCH_SUBS)
    print("The FastTRAK Reddit Interface is now running. I am monitoring the following subs: \n")
    print(config.WATCH_SUBS + "\n")

    for comment in subreddit.stream.comments():
        if config.TRIGGER in comment.body:
            if str(comment.author) in reddit.list_mods(r):
                verb = comment.body.replace(config.TRIGGER, "")
                verb = verb[1:]
                reddit.parse_verb(verb, comment, r)
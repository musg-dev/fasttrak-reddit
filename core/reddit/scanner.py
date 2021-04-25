from core import config
import reddit
import mods
import plugins
import praw

def sub_scan(reddit):
    subreddit = reddit.subreddit(config.WATCH_SUBS)
    print("The FastTRAK Reddit Interface is now running. I am monitoring the following subs: \n")
    print(config.WATCH_SUBS + "\n")

    for comment in subreddit.stream.comments():
        if config.TRIGGER in comment.body:
            if str(comment.author) in mods.list_mods():
                verb = comment.body.replace(trigger_phrase, "")
                verb = verb[1:]
                parse_verb(verb)
                
                
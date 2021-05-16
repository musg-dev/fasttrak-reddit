from bot import config
from . import router, mods


def sub_scan(r):
    subreddit = r.subreddit(config.WATCH_SUBS)
    print("The FastTRAK Reddit Interface is now running. I am monitoring the following subs: \n")
    print(config.WATCH_SUBS + "\n")

    for comment in subreddit.stream.comments():
        if config.TRIGGER in comment.body:
            if str(comment.author) in mods.list_mods(r):
                verb = comment.body.replace(config.TRIGGER, "")
                verb = verb[1:]
                router.parse_verb(verb, comment, r)

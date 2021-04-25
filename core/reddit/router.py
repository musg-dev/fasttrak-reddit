import praw
from sentry_sdk import capture_message
import reddit

def parse_verb(verb, comment, r):
    if verb == "secure":
        thread_id = comment.link_id[3:]
        submission = r.submission(id=thread_id)
        if submission.mod.thing.locked != True:
            count = reddit.tabulate_votes(submission, thread_id)
            reddit.secure_thread(submission, count)
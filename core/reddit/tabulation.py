import reddit
from sentry_sdk import capture_message
import praw
import datetime
import reddit

# Variables

aye = 0
nay = 0
abst = 0


def clear_vars():
    aye = 0
    nay = 0
    abst = 0


def tabulate_votes(submission, thread_id):
    print(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [INFO] Securing Thread " + thread_id + ".")
    capture_message(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [INFO] Securing Thread " + thread_id + ".")
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    comm_count = len(all_comments)
    for i in all_comments:
        if reddit.parse_vote(i.body) == 1:
            aye + 1
        if reddit.parse_vote(i.body) == 0:
            nay + 1
        if reddit.parse_vote(i.body) == 2:
            abst + 1
        else:
            print(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [WARN] Parser Mismatch (" + i.id + ").")
            capture_message(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [WARN] Parser Mismatch (" + i.id + ").")
    count = [aye], [nay], [abst]
    return count



def secure_thread(submission, count):
    aye = count[0]
    nay = count[1]
    abst = count[2]
    submission.reply("THREAD IS SECURED! \n\n \n\n Ayes: " + str(aye) + " \n\n Nays: " + str(nay) + " \n\n Abstain: " + str(abst))
    submission.mod.lock()
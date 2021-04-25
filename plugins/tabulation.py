from core import reddit
from sentry_sdk import capture_message

# This plugin is used to automatically tabulate and secure bill threads.
#
#
#

# Variables

aye = 0
nay = 0
abst = 0


def clear_vars():
    aye = 0
    nay = 0
    abst = 0


def tabulate_votes(submission):
    print(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [INFO] Securing Thread " + thread_id + ".")
    capture_message(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [INFO] Securing Thread " + thread_id + ".")
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    comm_count = len(all_comments)
    for i in all_comments:
        if reddit.parser(i.body) == 1:
            aye + 1
        if reddit.parser(i.body) == 0:
            nay + 1
        if reddit.parser(i.body) == 2:
            abst + 1
        else:
            print(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [WARN] Parser Mismatch (" + i.id + ").")
            capture_message(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [WARN] Parser Mismatch (" + i.id + ").")

def secure_thread(submission):
    comment.reply("THREAD IS SECURED! \n\n \n\n Ayes: " + str(aye_count) + " \n\n Nays: " + str(nay_count) + " \n\n Abstain: " + str(abst_count))
    submission.mod.lock()
from re import sub
import emoji
from sentry_sdk import capture_message
import datetime
import bot_parser
import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import db_ops


engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)
s = Session()


def tabulate_votes(submission, thread_id):
    aye = 0
    nay = 0
    abst = 0
    alerts = 0
    print(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [INFO] Securing Thread " + thread_id + ".")
    capture_message(datetime.datetime.utcnow().isoformat() + " Plugins::Secure // [INFO] Securing Thread "
                    + thread_id + ".")
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    for i in all_comments:
        bid = db_ops.find_bill(submission, submission.id)
        tid = db_ops.find_thread(submission.id)
        uid = db_ops.find_user(i.author.id, i.author.name)
        if bot_parser.parse_vote(i.body, i.author.name) == 1:
            db_ops.create_vote(uid, bid, tid, 1)
            aye = aye + 1
        elif bot_parser.parse_vote(i.body, i.author.name) == 0:
            db_ops.create_vote(uid, bid, tid, 0)
            nay = nay + 1
        elif bot_parser.parse_vote(i.body, i.author.name) == 2:
            db_ops.create_vote(uid, bid, tid, 2)
            abst = abst + 1
        elif bot_parser.parse_vote(i.body, i.author.name) == 10:
            print(datetime.datetime.utcnow().isoformat() + ": Tabulation::Tabulate_Votes // [INFO] Ignoring Trigger.")
        else:
            print(datetime.datetime.utcnow().isoformat() + " Tabulation::Tabulate_Votes // [WARN] Parser Mismatch on thread ID: " + i.id + ".")
            capture_message(datetime.datetime.utcnow().isoformat() + " Tabulation::Tabulate_Votes // [WARN] Parser Mismatch on thread ID: "+ i.id + ".")
            alerts = alerts + 1
    count = [aye], [nay], [abst], [alerts]
    return count


def secure_thread(submission, count):
    aye = count[0]
    nay = count[1]
    abst = count[2]
    alerts = count[3]
    if alerts == [0]:
        db_ops.update_thread(submission.id, True, True)
        submission.reply("The thread has been secured. \n\n \n\n Ayes: " + str(aye) 
                                                        + " \n\n Nays: " + str(nay)
                                                        + " \n\n Abstain: " + str(abst))
    if alerts != [0]:
        db_ops.update_thread(submission.id, True, True)
        submission.reply(emoji.emojize(":biohazard:") + " I HAVE ALERTS! CHECK SENTRY! " + emoji.emojize(":biohazard:")
                         + " \n\n \n\n \n\n \n\n The thread has been secured with " + " " + str(alerts) 
                                             + " alerts. \n\n \n\n Ayes: " + str(aye) 
                                                          + " \n\n Nays: " + str(nay)
                                                          + " \n\n Abstain: " + str(abst))
    submission.mod.lock()
    s.close_all()

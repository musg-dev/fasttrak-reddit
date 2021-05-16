import emoji
from sentry_sdk import capture_message
import datetime
from . import bot_parser
from bot import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..db.first_run import models


engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)


def create_bill(sub, thr_id):
    s = Session()
    bill_type = bot_parser.parse_title(sub.title)
    bill_num = bot_parser.parse_bill_num(sub.title, bill_type)

    bill_full = models.Bills(
        bill_type=bill_type,
        bill_num=bill_num,
        last_seen=datetime.datetime.utcnow().isoformat(),
        last_seen_thread=thr_id
    )

    bill_query = models.Bills(
        bill_type=bill_type,
        bill_num=bill_num
    )

    s.close_all()

    if s.query(bill_query).first() is None:
        s.add(bill_full)
        s.commit()

    if s.query(bill_query).first() is not None:
        q = s.query(bill_query).first()
        q.last_seen=datetime.datetime.utcnow().isoformat()
        q.last_seen_thread=thr_id
        s.commit()
        sub.reply("Thread is enabled.")


def create_user(usr_id, usr_name):
    s = Session()

    usr_query = models.Redditors(
        user_api=usr_id
    )

    usr_full = models.Redditors(
        user_api=usr_id,
        user_friendly=usr_name,
        active=1,
        last_seen=datetime.datetime.utcnow().isoformat()
    )

    s.close_all()

    if s.query(usr_query).first() is None:
        s.add(usr_full)

    if s.query(usr_query).first() is not None:
        q = s.query(usr_query).first()
        q.last_seen = datetime.datetime.utcnow().isoformat()
        s.commit()


def find_user(usr_id):
    s = Session()

    usr_query = models.Redditors(
        user_api=usr_id
    )

    result = s.query(usr_query).first().id
    return result

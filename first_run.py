from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot import config
from . import models

engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)


def db_kickstart():
    models.Base.metadata.create_all(engine)
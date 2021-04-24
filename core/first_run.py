from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)

def first_run():
    models.Base.metadata.create_all(engine)
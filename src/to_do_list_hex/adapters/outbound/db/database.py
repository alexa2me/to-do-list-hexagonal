from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from to_do_list_hex.adapters.settings import settings

engine = create_engine(settings.DB_URL, pool_size=1, pool_timeout=15)


Session = sessionmaker(bind=engine)


def get_session():
    with Session() as session:
        yield session

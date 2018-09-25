import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from flaskapp.models import Base


@pytest.fixture(scope='function')
def db_session():
    engine = create_engine('sqlite:////tmp/test.db')
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.metadata.create_all(bind=engine)
    yield db_session
    Base.metadata.drop_all(bind=engine)

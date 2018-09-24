from sqlalchemy import Column, Integer, String

from flaskapp.database import Base


class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f'<Thing "{self.name}">'

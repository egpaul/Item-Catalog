import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


# class to store user info
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    image = Column(String(250))
    provider = Column(String(25))


# class for Whiskey Database
class WhiskeyDB(Base):
    __tablename__ = "whiskey"

    id = Column(Integer, primary_key=True)
    whiskeyName = Column(String(250), nullable=False)
    avgPrice = Column(String(250), nullable=False)
    description = Column(String(), nullable=False)
    category = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # return whiskey data in serializable format
        return {
            'id': self.id,
            'name': self.whiskeyName,
            'price': self.avgPrice,
            'description': self.description
            'category': self.category,
        }


engine = create_engine('sqlite:///WhiskeyCatalog.db')
Base.metadata.create_all(engine)

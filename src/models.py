import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Stories(Base):
    __tablename__ = 'Stories'
    id = Column(Integer, primary_key = True)
    media = Column(String(150), nullable = False)
    views = Column(String(150))
    likes = Column(String(150))
    profile_id = Column(Integer, ForeignKey('profile.id'))

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key = True)
    media = Column(String(150), nullable = False)
    copy = Column(String(150))
    likes = Column(Integer)
    comments = Column(String(500))
    profile_id = Column(Integer, ForeignKey('profile.id'))

class Profile(Base):
    __tablename__ = 'Profile'
    id = Column(Integer, primary_key = True)
    profile_pic = Column(String(150))
    bio = Column(String(150))
    followers = Column(String(150))
    following = Column(String(150))
    user_id = Column(Integer, ForeignKey('user.id'))
    stories = relationship(Stories)
    post = relationship(Post)

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True)
    name = Column(String(150), nullable = False)
    email = Column(String(150), nullable = False)
    password = Column(String(150), nullable = False)
    profile = relationship(Profile)    
    
    
def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from xmlrpc.client import Boolean
from .database import Base
from  sqlalchemy import TIMESTAMP, Column, ForeignKey,Integer,String,Boolean

class Post(Base):
    __tablename__ ="posts"
    
    id =Column(Integer,primary_key= True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,nullable=False,server_default="True")
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner =relationship("User")
    
class User(Base):
    __tablename__ ="users"
    
    email =Column(String,nullable=False,unique= True)
    password=Column(String,nullable=False)
    id =Column(Integer,nullable=False,primary_key=True)
    created_at= Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    phone_number =Column(Integer,nullable=True)
    age =Column(String,nullable=True)
    

class Vote(Base):
    __tablename__ ="votes"
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    
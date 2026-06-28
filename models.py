from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
# To convert this class into a model we inherit a base class
Base = declarative_base()
# declarative base returns our base class from ORM as output
class Task(Base):
    __tablename__ = "task"
    task_id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False)
    status = Column(Boolean,default=False)
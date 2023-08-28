from sqlalchemy import Column, Integer, String, TIMESTAMP
from config import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    dueDate = Column(String, nullable=False)

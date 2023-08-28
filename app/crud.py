from sqlalchemy.orm import Session
from models import Task
from schemas import TaskSchema


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task: TaskSchema):
    db_task = Task(title=task.title,
                   description=task.description, dueDate=task.dueDate)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(db_task)
    db.commit()


def update_task(db: Session, task_id: int, task: TaskSchema):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db_task.title = task.title
    db_task.description = task.description
    db_task.dueDate = task.dueDate
    db.commit()
    db.refresh(db_task)
    return db_task

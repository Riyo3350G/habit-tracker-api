from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.task_model import Task  # SQLAlchemy model
from app.views.task_view import TaskCreate, Task as TaskPydantic  # Pydantic model
from app.core.database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=list[TaskPydantic])
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return [db_task]

@router.get("/", response_model=list[TaskPydantic])
def read_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()  # Uses SQLAlchemy Task model
    return tasks
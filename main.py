from fastapi import FastAPI
from app.controllers import task_controller, user_controller
from app.core.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Habit Tracker API - MVC")

# Include controllers
app.include_router(task_controller.router)
app.include_router(user_controller.router)

@app.get("/")
def root():
    return {"message": "🚀 Habit Tracker API (MVC) is running"}

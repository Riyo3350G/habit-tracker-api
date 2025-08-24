from fastapi import FastAPI

app = FastAPI(title="Habit Tracker API")


@app.get("/")
def root():
    return {"message": "Welcome to the Habit Tracker API"}



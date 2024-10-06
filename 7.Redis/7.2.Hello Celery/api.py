from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
from celery_tasts import app, greet, create_dummy_file  # Import the necessary tasks


app = FastAPI()


class TaskOut(BaseModel):
    id: str
    status: str


@app.get("/start")
def start() -> TaskOut:
    r = create_dummy_file.delay()  # Call the correct task
    return _to_task_out(r)


@app.get("/status/{task_id}")
def status(task_id: str) -> TaskOut:
    r = AsyncResult(task_id, app=app)  # Correctly create AsyncResult with app reference
    return _to_task_out(r)


def _to_task_out(r: AsyncResult) -> TaskOut:
    return TaskOut(id=r.task_id, status=r.status)

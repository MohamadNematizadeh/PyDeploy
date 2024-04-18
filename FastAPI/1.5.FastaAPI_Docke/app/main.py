
import numpy as np
import io
from asyncio import tasks
from fastapi import FastAPI,File,Form,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from insightface.app import FaceAnalysis
from app.databes import Table

db = Table()
app = FastAPI()

@app.get("/")
async def read():
    return db.read_data()
    
# def post
@app.post("/tasks")
def insert_data(title: str=Form(),description:str=Form(),status:str=Form(),time:str=Form()):
    resalt_sql = db.add_new_task(title,description,status,time)
    if resalt_sql ==True:
        return "YES"
    else:
        return"NO"
  
# def delete
@app.delete("/tasks/{id}")
def delete(id:str):
    data = db.delet_tasks(id)
    if data == True:
        return {"message":"successful"}

    if data == False:
        raise HTTPException(status_code=400 , detail="Task Can not be deleted , because this id does not exists in database")
    
# def updata
@app.put("/tasks/{id}")
def update(id:str):
    data = db.task_done(id)
    if data == True:
        return {"message":"successful"}
    if data == False:
        raise HTTPException(status_code=404,detail="not pag")


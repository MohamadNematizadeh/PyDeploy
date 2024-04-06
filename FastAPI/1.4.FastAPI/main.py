import cv2
import numpy as np
import io
from asyncio import tasks
from fastapi import FastAPI,File,Form,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from face.src.FaceIdentification import FaceIdentification
from insightface.app import FaceAnalysis
from database import Table

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



@app.post("/image")
async def upload_imag(input_file:UploadFile=File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415,detail="file not typ")
    contents = await input_file.read()
    array = np.frombuffer(contents,dtype=np.uint8)
    image = cv2.imdecode(array,cv2.IMREAD_UNCHANGED)
    app = FaceAnalysis(name="buffalo_s",providers=['CPUExecutionProvider'])
    app.prepare(ctx_id=0,det_size=(640,640))
    input_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    face_bank = np.load("face/face_bank.npy",allow_pickle=True)
    results = app.get(input_image)
    result = FaceIdentification.draw_bounding_box(results,input_image,face_bank)
    result = cv2.cvtColor(result,cv2.COLOR_BGR2RGB)
    _, encode_image = cv2.imencode(".jpg", result)
    return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type = "image/jpeg")


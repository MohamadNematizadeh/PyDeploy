import io
from typing import List, Tuple
from fastapi import FastAPI, File, UploadFile ,HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import cv2
from src.face_analysis import FaceAnalysis
import base64

app = FastAPI()

face_analysis = FaceAnalysis("models/det_10g.onnx", "models/genderage.onnx")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/analyze-face")
async def analyze_face(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        np_array = np.frombuffer(image_data, np.uint8)
        image_cv2 = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        print("Image decoded successfully")
        output_image, genders, ages = face_analysis.detect_age_gender(image_cv2)
        
        _, encoded_image = cv2.imencode('.jpg', output_image)
        image_base64 = base64.b64encode(encoded_image).decode('utf-8')
        
        result = {
            "genders": genders,
            "ages": ages,
            "image": image_base64,
        }
        
        return JSONResponse(content=result)

    except Exception as e:
        print(f"Error processing image: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
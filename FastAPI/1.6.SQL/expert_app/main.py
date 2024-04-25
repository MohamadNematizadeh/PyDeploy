from fastapi import FastAPI, Depends, HTTPException

from database import engine
import models as models
import schemas as schemas
from crud import University_System

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read():
   return print("welcam to api University System  🧑🏻‍🎓")

@app.get("/students", response_model=schemas.Student)
def student_read(id: int ):
    db = University_System.student_red(db, student_id=id)
    if db is None:
        raise HTTPException(status_code=404, detail="users not")
    return db


@app.post("/students", response_model=schemas.Student)
def student_create(student: schemas.StudentCreate):
    db = University_System.student_create(student=student)
    return db

@app.put("/students", response_model=schemas.Student)
def student_update(student_id: int,student: schemas.StudentCreate):
    db = University_System.student_update(student_id=student_id, student=student)
    return db

@app.delete("/students/{student_id}")
def student_delete(student_id:int):
    db_student = University_System.student_delete(student_id=student_id)
    return db_student


@app.get("/courses", response_model=schemas.Course)
def read_course(course_id : int, ):
    db_course = University_System.course_get(course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course

@app.post("/courses", response_model=schemas.Course)
def course_create(id : int, course: schemas.CourseCreate):
    db_course = University_System.course_create(course=course,id=id)
    return db_course

@app.put("/courses", response_model=schemas.Course)
def course_update(course_id: int,course: schemas.CourseCreate, ):
    db_course = University_System.course_update(course_id=course_id,  course=course)
    return db_course

@app.delete("/courses/{course_id}")
def course_delete(course_id:int):
    db_course = University_System.course_delete(course_id=course_id)
    return db_course
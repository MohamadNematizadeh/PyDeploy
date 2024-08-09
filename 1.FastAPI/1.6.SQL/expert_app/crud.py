from fastapi import  HTTPException
import models, schemas
from database import SessionLocal

class University_System():
        def __init__(self):
            self.db = SessionLocal()
            try:
                    yield self.db
            finally:
                    self.db.close()
  
        def student_red(self,student_id: int):
            return self.db.query(models.Student).filter(models.Student.id == student_id).first()
        
        def student_create(self, student: schemas.StudentCreate):
            db_student = models.Student(firstname=student.firstname, lastname=student.lastname, average = student.average, graduated = student.graduated)
            self.db.add(db_student)
            self.db.commit()
            self.db.refresh(db_student)
            return db_student
        
        def student_update(self,student_id:int, student: schemas.StudentCreate):
            db_student =  self.db.query(models.Student).filter(models.Student.id == student_id).first()
            if db_student is None:
                raise HTTPException(status_code=404, detail="Student not found")
            
            db_student.firstname = student.firstname
            db_student.lastname = student.lastname
            db_student.average = student.average
            db_student.graduated = student.graduated
            self.db.commit()
            self.db.refresh(db_student)
            return db_student

        def student_delete(self, student_id:int):
            student = self.db.query(models.Student).filter(models.Student.id == student_id).first()
            if student is None:
                raise HTTPException(status_code=404, detail="Student not found")
            self.db.delete(student)
            self.db.commit()
            return "Student removed"

        def course_get(self, course_id :int):
            return self.db.query(models.Course).filter(models.Course.id == course_id).first()

        def course_create(self, course: schemas.CourseCreate, id:int):
            db_course = models.Course(name=course.name, unit=course.unit, owner_id=id)
            self.db.add(db_course)
            self.db.commit()
            self.db.refresh(db_course)
            return db_course
        
        def course_update(self,course_id:int, course: schemas.StudentCreate):
            db_course =  self.db.query(models.Course).filter(models.Course.id == course_id).first()
            if db_course is None:
                raise HTTPException(status_code=404, detail="Course not found")

        def course_delete(self, course_id:int):
            course = self.db.query(models.Course).filter(models.Course.id == course_id).first()
            if course is None:
                raise HTTPException(status_code=404, detail="Course not found")
            self.db.delete(course)
            self.db.commit()
            return "Course removed"
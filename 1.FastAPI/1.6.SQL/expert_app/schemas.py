from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str
    unit: int 


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    owner_id: int


class StudentBase(BaseModel):
    firstname : str
    lastname : str
    average : float
    graduated : bool


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

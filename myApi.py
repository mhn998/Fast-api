# print('Hello World!!')
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    },
    2: {
        "name": "Mugh",
        "age": 23,
        "year": "year 100"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: Optional[int] = None):
    print(student_id)
    if (student_id):
        return students[student_id]
    else:

        return {"Hi!"}


@app.get("/get-by-name")
def get_student(year: str = None):
    for student_id in students:
        if students[student_id]["year"] == year:
            return students[student_id]

    return {"Data: Not Found!"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]


@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error : Student doesnt exist"}

    # This will set eveything to null if not updated.
    # To only update what is updated
    # if student.age != None:
        # student[student_id].age = student.age

    # if student.name != None:
        # student[student_id].name = student.name
    # if student.year != year:
        # student[student_id].age = student.age

    students[student_id] = student
    return students[student_id]


@app.delete("delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error : Tudent doesnt exist"}

    del students[student_id]
    return {"Message : Deleted Successfully!"}

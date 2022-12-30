from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.server.database import *
from app.server.models.schema import *


router = APIRouter()


@router.post("/", response_description="student data added to the database")
async def new_student(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add(student)

@router.get("/all", response_description="Students Data Retrieved")
async def get_all_students():
    students = await get_all()
    if students:
        return ResponseModel(students, "Retrieved all students data")
    ErrorModel("An Error Occurred", 404, "No Students database found")

@router.get("/{PIN}", response_description="student data retrieved")
async def get_student(PIN: str):
    student = await get(PIN)
    if student:
        return ResponseModel(student, f"Student data with PIN {PIN} retrieved")
    return ErrorModel("An Error occurred", 404, f"Student with PIN {PIN} does not exist")

@router.put("/{PIN}")
async def update_student_data(PIN: str, data: UpdateStudentModel = Body(...)):
    data = {k : v for k, v in data.dict().items() if v is not None}
    updated_student = await update(PIN, data)
    if updated_student:
        return ResponseModel(updated_student, f"{PIN} data updated")
    return ErrorModel("An Error occurred", 404, "Cannot update the data")

@router.delete("/delete/{PIN}", response_description="Delete student from database")
async def delete_student(PIN: str):
    student = await delete(PIN)
    if student:
        return ResponseModel(f"Student with {PIN} removed from the database", "Operation Success")
    return ErrorModel("An Error occurred", 404, f"student with PIN {PIN} does not exist")
    
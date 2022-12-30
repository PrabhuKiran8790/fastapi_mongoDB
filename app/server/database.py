import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

students_collection = database.get_collection("Student_Collections")

# helper
# converts student json object from mongodb to python dictionary
def student_helper(student) -> dict:
    return {
        "id" : str(student["_id"]),
        "fullname" : student["fullname"],
        "email" : student["email"],
        "PIN" : str(student["PIN"]),
        "course" : student["course"],
        "year" : student["year"],
        "gpa" : student["gpa"]
    }
    
# crud operations

async def get_all():
    students = []
    async for student in students_collection.find():
        students.append(student_helper(student))
    return students

async def add(student_data: dict) -> dict:
    student = await students_collection.insert_one(student_data)
    new_student = await students_collection.find_one({"_id" : student.inserted_id})
    return student_helper(new_student)

async def get(PIN: str) -> dict:
    student = await students_collection.find_one({"PIN" : PIN})
    if student:
        return student_helper(student)
    
async def update(PIN: str, updated_data: dict) -> dict:
    if not updated_data:
        return False
    student = await students_collection.find_one({"PIN" : PIN})
    if student:
        students_collection.update_one({"PIN" : PIN}, {"$set" : updated_data})
        return True
    return False 

async def delete(PIN: str):
    student = await students_collection.find_one({"PIN" : PIN})
    if student:
        await students_collection.delete_one({"PIN" : PIN})
        return True
    return False
    
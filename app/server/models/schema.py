from typing import Optional
from pydantic import EmailStr, BaseModel, Field

class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    PIN: str = Field(...)
    course: str = Field(...)
    year: int = Field(..., gt=0, le=4)
    gpa: float = Field(..., le=10.0)
    
    class Config:
        schema_extra = {
            "example" : {
                "fullname" : "Prabhu Kiran Konda",
                "email" : "prabhukiran426@gmail.com",
                "PIN" : "20K45A0215",
                "course" : "Electrical and Electronics Engineering",
                "year" : 4,
                "gpa" : 8.5,
            }
        }
        
        
class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email:  Optional[EmailStr]
    PIN: Optional[str]
    course: Optional[str]
    year: Optional[int]
    gpa: Optional[float]
    
    class Config:
        schema_extra = {
            "example" : {
                "fullname" : "Prabhu Kiran Konda",
                "email": "prabhukiran426@outlook.com",
                "PIN" : "20K45A0215",
                "course" : "Electrical and Electronics Engineering",
                "year" : 4,
                "gpa" : 8.5,
            }
        }
    
def ResponseModel(data, message):
    return {
        "data" : data, 
        "message" : message
    }
    
    
def ErrorModel(error, code, message):
    return {
        "error" : error,
        "code" : code,
        "message" : message
    }

    
    
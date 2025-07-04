from fastapi import APIRouter,HTTPException,status
from app.schemas.student_schema import Student
from app.utils.logger import logger
import app.db as db

router=APIRouter()

@router.post("/students/",status_code= status.HTTP_201_CREATED)
async def add_student(student:Student):
    try:
        logger.info("Adding student: %s",student.dict())
        student_collection=db.get_students_collection()
        result =student_collection.insert_one(student.dict()) 
        logger.debug("Student inserted with ID: %s",str(result.inserted_id))
        return{
            "message":"Student added sucessfully",
            "data": student.dict(),
            "id": str (result.inserted_id)
            
        }
    except Exception as e : 
        logger.exception("Faild to add student")
        raise HTTPException(status_code=500, detail="Internal server error")
    
@router.get("/student/",status_code=status.HTTP_200_OK)
async def get_student():
    try:
        logger.info("retreving student data ")
        Student_collection=db.get_students_collection()
        students=list(Student_collection.find({},{"_id": 0}))
        logger.debug("Total students fetched : %d", len(students))
        return {"student":students}
    except Exception as e :
        logger.exception("Failed to fetch students")
        raise HTTPException(status_code=500, detail="Internal Server Error")

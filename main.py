
from fastapi import FastAPI
from app.routers.student_router import router as student_router

app = FastAPI()

app.include_router(student_router)
@app.get("/")
def home_page():
    return {"message": "Student API is successfully working"}
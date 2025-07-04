from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]

def get_students_collection():
    return db["student"]  
    
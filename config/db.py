#Here is the part that connects FastAPI TO mongoDB
from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27107")
db = conn.task2
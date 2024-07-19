from pymongo import MongoClient

client = MongoClient("mongodb+srv://berarney:Qwoipt67@cluster0.v1eszj7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.edu_db
collection_name = db["edu_collection"]
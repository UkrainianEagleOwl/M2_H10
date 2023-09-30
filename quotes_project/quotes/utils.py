from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_mongo_db():
    uri = "mongodb+srv://dmytrofilin:SV3s7TTyNsljL5Zp@ukrainianeagleowl.bvkh16q.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    db = client.M2_H08
    
    return db
from pymongo import MongoClient
from pymongo.server_api import ServerApi


MONGO_URI = "mongodb+srv://jungle000ww:000gustavo@cluster0.4gxzomt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client["Mongo-shortURL"]


db = client.shorturl_db

collection_name = db["url_collection"]

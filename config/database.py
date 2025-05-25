from pymongo import MongoClient

client = MongoClient("mongodb+srv://jungle000ww:000gustavo@cluster0.4gxzomt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.shorturl_db

collection_name = db["url_collection"]

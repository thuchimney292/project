import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb://thangnq:12345678Abc@cluster0-shard-00-00-zqxy8.mongodb.net:27017,cluster0-shard-00-01-zqxy8.mongodb.net:27017,cluster0-shard-00-02-zqxy8.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.all_book
def get_book(theloai):
    return list(db[theloai].find())
def sortt():
    return db.all.find()

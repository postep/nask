import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient()
client = MongoClient('localhost', 27017)

db = client["alerts"]
iptables_collection = db["iptables_block"]
alert = {"ip": "Mike", "description": "try of nmap", "date": datetime.datetime.utcnow()}
x = iptables_collection.insert_one(alert)
print(x)
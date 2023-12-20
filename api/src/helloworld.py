from pymongo import MongoClient

print("hallo")

client = MongoClient("mongodb://root:example@mongo:27017")
db = client.testdb

try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")

client.close()

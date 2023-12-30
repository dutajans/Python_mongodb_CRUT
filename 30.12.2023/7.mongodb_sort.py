from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# sort dökümanların artan sırada (ascending) sıralar
results = collection.find({}, {"_id": 0, "name":1, "salary":1}).sort("salary")
for result in results:
    print(result)

# Azalan sıralama more readable
query = {
    "$or": [
        {"name": {"$regex": "[aeiou]$"}},
        {"salary": {"$gt": 55000}}
    ]
}
projection = {
    "_id": 0,
    "name": 1,
    "salary":1
}

results = collection.find(query, projection)
for result in results.sort("salary", -1):
    print(result)

# sort by multiple fileds
results = collection.find(query, projection)
for result in results.sort([("salary", -1),("name", 1)]):
    print(result)

client.close()
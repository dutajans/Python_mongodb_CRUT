from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# QUERY OPERATORS

# $gt (greater than) operatörü
query   = {"address": {"$gt": "S"}}
results = collection.find(query)

print("Documents with address greater than 'S':")
for result in results:
    print(result)

# Maaşı (salary) 50000'den büyük olan kayıtlar
query = {"salary": {"$gt": 50000}}
projection = {"_id": 0, "name": 1, "salary": 1}
results = collection.find(query, projection)

print("Documents with salary greater than 50000:")
for result in results:
    print(result)


# less than ($lt)
query = {"salary": {"$lt": 55000}}
projection = {"_id": 0, "name": 1, "salary": 1}
results = collection.find(query, projection)

print("Documents with salary less than 55000:")
for result in results:
    print(result)

# greater than or equal ($gte)
# less than or equal to ($lte)

# equal to ($eq)
# not equal to ($ne)

# in ($in)
query = {"address": {"$in": ["Sunset Blvd 123", "Hillside Ave 789", "Forest Rds 123"]}}
projection = {"_id": 0, "name": 1, "address": 1}
results = collection.find(query, projection)

for result in results:
    print(result)

# $regex operatörü
query = {"address": {"$regex": "^Hill"}}
projection = {"_id": 0, "name": 1, "address": 1}
results = collection.find(query, projection)

for result in results:
    print(result)

# 'addres' field A-H ile başlayan
query = {"address": {"$regex": "^[A-H]"}}
projection = {"_id": 0, "name": 1, "address": 1}
results = collection.find(query, projection)

for result in results:
    print(result)

# 'name' field'ının sonu sesli harfle bitecek, 'salary' 55000'den yüksek olan dokümnları
query = {"name": {"$regex": "[aeiou]$"}, "salary": {"$gt": 55000}}
projection = {"_id": 0}
results = collection.find(query, projection)

for result in results:
    print(result)

# $and operatörü
query = {
    "$and": [
        {"name": {"$regex": "[aeiou]$"}},
        {"salary": {"$gt": 55000}}
    ]
}
projection = {"_id": 0}
results = collection.find(query, projection)

for result in results:
    print(result)

# $and operatörü
query = {
    "$or": [
        {"name": {"$regex": "[aeiou]$"}},
        {"salary": {"$gt": 55000}}
    ]
}
projection = {"_id": 0}
results = collection.find(query, projection)

for result in results:
    print(result)

# $or operatörü
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

for result in results:
    print(result)

client.close()
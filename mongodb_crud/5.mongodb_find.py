from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Bir Query (Sorgu) olmaksızın find()
mydocs = collection.find()

print("All Documents")
for doc in mydocs:
    print(doc)

mydocs = collection.find()
for doc in mydocs:
    print(doc["name"])

mydocs = collection.find()
for doc in mydocs:
    print(doc["age"]) # KeyError: 'age' burayı ilerde işleyeceğiz

# Bir Query ile Find()
query = {"salary": 50000}
mydocs = collection.find(query)

for doc in mydocs:
    print(doc)

# Query ve Projection beraber kullanımı
query = {"salary": 50000}       # filtreleme
projection = {"_id": 0, "address": 1}   # field seçimi

mydocs = collection.find(query, projection)

for doc in mydocs:
    print(doc)

###
query = {"salary": 50000}   # filtreleme
projection = {"_id": 0, "name": 1, "address": 1}    # field seçimi

mydocs = collection.find(query, projection)

for doc in mydocs:
    print(doc)

###
query = {"salary": 50000}   # filtreleme
projection = {"_id": 0, "address": 1}   # field seçimi

mydocs = collection.find(query, projection)

for doc in mydocs:
    print(doc)

###
query = {"salary": 60000}   # filtreleme
projection = {"_id": 1, "name": 0,}   # field seçimi

mydocs = collection.find(query, projection)

for doc in mydocs:
    print(doc)

# Bir sorgu daha
mydocs = collection.find({}, {"_id": 0, "name": 1, "salary":1})
for doc in mydocs:
    print(doc)

mydocs = collection.find({}, {"_id": 0, "address":0})
for doc in mydocs:
    print(doc)

client.close()
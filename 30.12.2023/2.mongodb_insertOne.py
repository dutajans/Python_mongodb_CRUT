from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Bir döküman oluşturmak
mydict = {
    "name": "John",
    "address": "Highway 37",
    "salary": 50_000
}

 # Koleksiyona bir döküman eklemek
 mydoc = collection.insert_one(mydict)

 print(mydoc)
 print(type(mydoc))
 print(mydoc.inserted_id)


# Bir döküman oluşturmak
mydict2 = {
    "name": "Peter",
    "address": "Lowstreet 27",
    "salary": 60_000
}

mydoc2 = collection.insert_one(mydict2)
print(mydoc2)
print(type(mydoc2))
print(mydoc2.inserted_id)

# Bir döküman oluşturmak
mydict3 = {
    "name": "Peter22",
    "address": "Lowstreet 27",
    "salary": 60_000,
    "age": 50
}

mydoc = collection.insert_one(mydict3)
print(mydoc)
print(type(mydoc))
print(mydoc.inserted_id)

mydict4 = {
    "address": "Lowstreet 27",
    "age": 50,
    "name": "Yunus",
    "surname": "Yıldız",
    "salary": 60_000,
    "city": "ankara"

}

mydoc = collection.insert_one(mydict4)
print(mydoc)
print(type(mydoc))
print(mydoc.inserted_id)

client.close()
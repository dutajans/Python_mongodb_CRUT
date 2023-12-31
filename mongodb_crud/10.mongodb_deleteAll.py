from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Yeni bir koleksiyon oluştur.
collection = db["programs"]

program = {
    "name": "MongoDB",
    "type": "Databese",
    "initial_relase": 2009,
    "scalability": "High",
    "performance": "Fast",
    "creator": "MongoDB Inc."
}

# Dökümanı ekleyelim
mydoc = collection.insert_one(program)
print("Insorted Document ID:", mydoc.inserted_id)





programs2 = [
    {
        "name": "Python",
        "type": "Programming Language",
        "initial_release": 1991,
        "scalability": "High",
        "performance": "High",
        "creator": "Guido van Rossum"
    },
    {
        "name": "Java",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "High",
        "performance": "Medium",
        "creator": "James Gosling"
    },
    {
        "name": "JavaScript",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Brendan Eich"
    },
    {
        "name": "C++",
        "type": "Programming Language",
        "initial_release": 1985,
        "scalability": "High",
        "performance": "High",
        "creator": "Bjarne Stroustrup"
    },
    {
        "name": "MySQL",
        "type": "Database",
        "initial_release": 1995,
        "scalability": "High",
        "performance": "High",
        "creator": "MySQL AB"
    },
    {
        "name": "Ruby",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Yukihiro Matsumoto"
    },
    {
        "name": "PHP",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Rasmus Lerdorf"
    },
    {
        "name": "TensorFlow",
        "type": "Machine Learning Library",
        "initial_release": 2015,
        "scalability": "High",
        "performance": "High",
        "creator": "Google Brain Team"
    },
    {
        "name": "Apache CouchDB",
        "type": "Database",
        "initial_release": 2005,
        "scalability": "High",
        "performance": "High",
        "creator": "Apache Software Foundation"
    }
]

mydocs = collection.insert_many(programs2)
print(mydocs)
print(mydocs.inserted_ids)

mydocs = collection.find()

print("All Documents")
for doc in collection.find({}, {"_id": 0, "name": 1, "type": 1}):
    print(doc)


# type alanı "Database" veya "Machine Learning Library" olan dökümanları bulun.
types = ["Database", "Machine Learning Library"]
query = {"type": {"$in": types}}
projection = {"_id": 0, "name": 1, "type": 1}
results = collection.find(query, projection)

for result in results:
    print(result)


# $or operatörü
query = {
    "$or": [
        {"type": "Database"},
        {"type": "Machine Learning Library"}
    ]
}
projection = {
    "_id": 0,
    "name": 1,
    "type":1
}
results = collection.find(query, projection)

for result in results:
    print(result)


# Tipi "Database" olanları silin
result = collection.delete_many({"type": "Database"})
print("Deleted Documents: ", result.deleted_count)

# Tüm dökümanları silin
result = collection.delete_many({})
print("Deleted Documents: ", result.deleted_count)


client.close()
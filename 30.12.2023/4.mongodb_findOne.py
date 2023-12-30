from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Bir Query (Sorgu) olmaksızın find_one()
result = collection.find_one()
print(result) # <class 'dict'>
print(type(result))

print(f"Name: {result['name']}\nAddress: {result['address']}\nSalary: {result['salary']}")

# Bir Query (Sorgu) ile find_one()
query = {"name": "Peter"}   # filtreleme
result = collection.find_one(query)   # sadece bir doküman
print(f"Name: {result['name']}\nAddress: {result['address']}\nSalary: {result['salary']}")

client.close()


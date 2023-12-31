from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

query = {"address": "Mountain 21"}

result = collection.delete_one(query)

print("Deletion Acknowledged", result.acknowledged)
print("Number of Documents Deleted", result.deleted_count)

# deleteOne() query'le eşleşen ilk dokümanı siler. Spesifik bir dokümanı silmek için
# _id alanı (field) query'de kullanılmalıdır.

result = collection.delete_one({"_id": 7})
print("Number of Documents Deleted", result.deleted_count)

client.close()
##################.#################


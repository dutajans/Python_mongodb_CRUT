from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Spesifik bir adresi bulup bu adresi güncelemek
query = {"address": "Valley 345"}   # filterliyoruz
new_value = {"$set": {"address": "Canyon 123"}} # güncelleme operatörü kullanıyoruz.

result = collection.update_one(query, new_value)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)


client.close()
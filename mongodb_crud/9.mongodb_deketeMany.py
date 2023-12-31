from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Adresi S ile başlayan dökümanların hepsini silelim.
query = {"address": {"$regex": "^S"}}
result = collection.delete_many(query)

print("Deletion Acknowledged", result.acknowledged)     # Silinme işleminin Başarısı
print("Deletion Acknowledged", result.deleted_count)    # Silinen döküman sayısı
print("Raw Result:", result.raw_result)                 # İşlemin Sonucu

client.close()
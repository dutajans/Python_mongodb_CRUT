from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# Limit gelen sorguyu sınırlandırıyor arama filtresine uygun şekilde son 3 değeri istedik aşağıda geldi.
query = {"income": {"$gt": 61000}}
projection = {"_id":0, "name":1, "income":1}
result = collection.find(query, projection).sort("income", -1).limit(3)
for item in result:
    print(item)

# 'name' field [A-H]
# 'income' 61000'den küçük olanları 2700 artıralım.
# 'income' 61000'den büyük olanları %5 artıralım.
# tüm dökümanları income alanına göre azalan şekilde yazdıralım
# sadece 'name' ve 'income' alanları yazdırılsın.
# ilk 5 döküman yazdırılsın.
query1 = {
    "name": {"$regex": r"^[A-M]"},
    "income": {"$lt": 61000}
}
query2 = {
    "name": {"$regex": r"^[A-M]"},
    "income": {"$gte": 61000}
}
update1 = {"$inc": {"income": 2700}}
update2 = {"$mul": {"income": 1.05}}

result1 = collection.update_many(query1, update1)
result2 = collection.update_many(query2, update2)

print("1. Değiştirilen: ", result1.modified_count)
print("2. Değiştirilen: ", result2.modified_count)

mydocs = collection.find({}, {"_id": 0, "name": 1, "income": 1}).sort("income", -1).limit(5)
for doc in mydocs:
    print(doc)

client.close()
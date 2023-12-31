import datetime
import pytz
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

# $SET UPDATE OPERATOR
# "address" alanı "M" ile başlayan müşterilerin "name" alanını "Minnie" yap.
query = {"address": {"$regex": r"^M"}}
update = {"$set": {"name": "Minnie"}}

result = collection.update_many(query, update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı", result.modified_count)

# $INC UPDATE OPERATOR
# Maaşı 55000'den küçük olanların maaşını 5000 artıralım.
query = {"salary": {"$lte": 55000}}
update = {"$inc": {"salary": 5300}}
result = collection.update_many(query, update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)


# Maaşı 58500'den büyük olanların maaşını 5300 azaltalım.
query = {"salary": {"$gte": 58_500}}
update = {"$inc": {"salary": -5300}}
result = collection.update_many(query, update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)

# $RENAME UPDATE OPERATOR
# 'salary' alanının ismini 'income' olarak değiştirin.
query = {}
update = {"$rename": {"salary": "income"}}

result = collection.update_many(query,update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)

# $CURRENTDATE UPDATE OPERATOR
query = {}
update = {"$currentDate": {"lastUpdated": True}}

result = collection.update_many(query,update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)

# Yerel Zamanı Atamak
now = datetime.datetime.now()
# print(now)
update = {"$set": {"lastUpdated": now}}
result = collection.update_many(query,update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)

# Farklı zaman dilimleri ile çalışmak
# import pytz
tokyo = pytz.timezone('Asia/Tokyo')
now = datetime.datetime.now(tokyo)
# print(now)
# print(type(tokyo))
now = now.strftime("%Y-%n-%d %H:%M")
update = {"$set": {"lastUpdated": now}}
result = collection.update_many(query,update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)

# $MUL UPDATE OPERATOR
query = {}
update = {"$mul": {"income": 1.1}}
result = collection.update_many(query,update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)

# Peter ile Any'nin maaşlarına %5 zam yapalım ve lastUpdate alanını güncelleyelim.
# { field: { $in: [<value1>, <value2>, ... <valueN> ] } }

now = datetime.datetime.now()
now = now.strftime("%Y-%n-%d %H:%M")
query = {"name": {"$in": ["Peter", "Amy"]}}
update = {
    "$mul": {"income": 1.05},
    "$set": {"lastUpdated": now}
}
result = collection.update_many(query,update)
print("Eşleşen dökümanların sayısı: ", result.matched_count)
print("Değiştirilen dökümanların sayısı: ", result.modified_count)

client.close()
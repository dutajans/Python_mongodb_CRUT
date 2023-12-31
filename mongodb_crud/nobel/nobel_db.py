import os
import json
from pymongo import MongoClient

yeni_dizin = 'C:/Users/Yunus/PycharmProjects/yunus/pythonmongodb/mongodb_crud/nobel/'

# Dizini değiştir
os.chdir(yeni_dizin)

# Şu anki dizini yazdır
print("Şu anki dizin:", os.getcwd())

client = MongoClient("mongodb://localhost:27017")
db = client["nobel"] # nobel veritabanı oluştur.

# nobelPrizes.json dosyasını yükle
with open('nobelPrizes.json', encoding="utf-8") as json_file:
    nobel_prizes_data = json.load(json_file)

# laured.json dosyasını yükle
with open('laureates.json', encoding="utf-8") as json_file2:
    laureates_data = json.load(json_file2)

# nobelPrizes koleksiyorunu oluştur ve dökümanları yükle
nobel_prizes_collection = db["nobel_prizes"]
result1 = nobel_prizes_collection.insert_many(nobel_prizes_data["nobelPrizes"])

print("İşlem başarılı: ", result1.acknowledged)

# "laureates" koleksiyonu oluştur ve dökümanları yükle
laureates_collection = db["laureates"]
result2 = laureates_collection.insert_many(laureates_data["laureates"])

print("İşlem Başarılı: ", result2.acknowledged)

print("Eklenen Dökümanların Sayısı: ", len(result2.inserted_ids))

# nobel_prizes koleksiyonundan kategorisi "Chemistry" kategorisine göre filtreleme sorgusu yazalım.

# İlk döngü
results = nobel_prizes_collection.find({"category.en": "Chemistry"})
for result in results:
    print(result.keys())

# İkinci döngü için tekrar sonuçları al
results = nobel_prizes_collection.find({"category.en": "Chemistry"})
for result in results:
    laureates = result["laureates"]
    for laureate in laureates:
        known_name = laureate["known_name"]["en"]

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]

collection_name = input("Silinecek koleksiyon adını giriniz:")
if "programs" in db.list_collection_names():
    collection = db[collection_name]
    collection.drop()
    print(f"{collection_name} isimli koleksiyon silindi.")
else:
    print(f"{collection_name} isimli bir koleksiyon mevcut değil.")

# Database Düşürmek
db_name = input("Silinecek database ismi: ")
if db_name in client.list_database_names():
    client.drop_database(db_name)
    print(f"{db_name} isimli database silindi.")
else:
    print(f"{db_name} isimli bir database mevcut değil.")

client.close()
# pip install pymongo Terminalde çalıştır.
from pymongo import MongoClient

# MongoDB sunucusuna bağlan
connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)

# Bir veritabanı oluşturmak ya da mevcut veritabanına erişmek
db = client["mydb"]

# Bir Koleksiyon (collection) oluşturmak veya mevcut koleksiyona erişmek
collection = db["customers"]

# Sistemdeki veritabanlarının listesi
print(client.list_database_names())

# Veritabanındaki koleksiyonların listesi
print(db.client.list_collections_names())

client.close()
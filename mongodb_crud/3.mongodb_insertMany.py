from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["customers"]

mylist = [{"name": "Amy", "address": "Apple st 652", "salary": 50000},
          {"name": "Hannah", "address": "Mountain 21", "salary": 60000},
          {"name": "Michael", "address": "Valley 345", "salary": 55000},
          {"name": "Sandy", "address": "Ocean blvd 2", "salary": 52000},
          {"name": "Betty", "address": "Green Grass 1", "salary": 53000},
          {"name": "Richard", "address": "Sky st 331", "salary": 58000},
          {"name": "Susan", "address": "One way 98", "salary": 54000},
          {"name": "Vicky", "address": "Yellow Garden 2", "salary": 57000},
          {"name": "Ben", "address": "Park Lane 38", "salary": 56000},
          {"name": "William", "address": "Central st 954", "salary": 59000},
          {"name": "Chuck", "address": "Main Road 989", "salary": 55000},
          {"name": "Viola", "address": "Sideway 1633", "salary": 60000}
          ] # list of dictoınaries

# 1'den çok döküman eklemek
mydocs = collection.insert_many(mylist)
print(mydocs)
print(mydocs.inserted_ids)

# ID'leri kendinizin verdigi durum
mylist2 = [
    {"_id": 1, "name": "Alice", "address": "Sunset Blvd 123", "salary": 50000},
    {"_id": 2, "name": "Bob", "address": "Ocean Ave 456", "salary": 60000},
    {"_id": 3, "name": "Eva", "address": "Rose St 789", "salary": 55000},
    {"_id": 4, "name": "Daniel", "address": "Mountain View Dr 321", "salary": 52000},
    {"_id": 5, "name": "Olivia", "address": "Lake Rd 654", "salary": 53000},
    {"_id": 6, "name": "Max", "address": "Pine St 987", "salary": 58000},
    {"_id": 7, "name": "Sophie", "address": "Meadow Ln 654", "salary": 54000},
    {"_id": 8, "name": "Jacob", "address": "Hillside Ave 789", "salary": 57000},
    {"_id": 9, "name": "Emily", "address": "Parkview Ct 987", "salary": 56000},
    {"_id": 10, "name": "Liam", "address": "Forest Rds 123", "salary": 59000},
    {"_id": 11, "name": "Isabella", "address": "Garden St 456", "salary": 55000},
    {"_id": 12, "name": "Noah", "address": "Maple Ave 789", "salary": 60000},
    {"_id": 13, "name": "Grace", "address": "Sycamore Ln 321", "salary": 61000},
    {"_id": 14, "name": "Henry", "address": "Cedar St 654", "salary": 57000}
]

mydocs = collection.insert_many(mylist2)
print(mydocs)
print(mydocs.inserted_ids)
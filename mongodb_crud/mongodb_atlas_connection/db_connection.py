from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://salimunlu:BilgeAdam*2023@trialcluster.o8r0nhj.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB.")
except Exception as e:
    print(e)

db = client['sample_airbnb']
collection = db['listingsAndReviews']

for doc in collection.find({"property_type": "House"}):
    print(doc)
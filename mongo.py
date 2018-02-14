import pymongo;
import urllib.request, json 
from pymongo import MongoClient;
url = "https://api.randomuser.me/?results=100";

client = MongoClient();
#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')
db = client.kashif;
collection = db.heros;
#print(collection)
print(db.collection_names(include_system_collections=False))
with urllib.request.urlopen(url) as url:
	data = json.loads(url.read().decode())
	results = data.get('results');
	collection.insert_many(results);

#for singleData in results:
	#print(singleData['gender'])
	#collection.insert_one(singleData)
	
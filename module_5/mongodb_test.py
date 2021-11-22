from pymongo import MongoClient

#password = 'Darlies10!'
#url = 'mongodb+srv://admin:' + password + '@cluster0.cgelx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

password = 'admin'
url = 'mongodb+srv://admin:' + password + '@cluster0.cgelx.mongodb.net/pytech'
client = MongoClient(url)

db = client.pytech

list_collection_names = db.list_collection_names()
print(list_collection_names)
import pymongo

from pymongo import MongoClient

name = 'yamural'
password = 'MKBd3gNDZeXJEXJX'
mongo_url =  f'mongodb+srv://{name}:{password}@yamcluster.b1wabqt.mongodb.net/?retryWrites=true&w=majority&appName=yamcluster'

cluster = MongoClient(mongo_url)
db = cluster['yam_db']
collection = db['users']


# collection.insert_one(
#     {
#         "_id":2,
#         'name': 'yamanu',
#         "score": 1.7
# })

post_1 = {"_id":3, "name":"yamany", "score":1.6}
post_2 = {"_id":4, "name":"yam", "score":1.9}
post_3 = {"_id":5, "name":"yamany"}


# collection.insert_many([post_1,post_2,post_3])
result = collection.find({"name":'yaman'})

for item in result:
    print(item["score"])




from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import json

client = MongoClient('localhost', 27017)
db = client['books']
catalog = db.catalog

with open('books.json', 'r') as f:
    data = json.load(f)

for book in data:
    try:
        catalog.insert_one(book)
    except DuplicateKeyError:
        print('Duplicate key error')
        continue

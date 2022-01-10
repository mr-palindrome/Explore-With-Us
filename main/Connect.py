import pymongo
import os
from decouple import config


client = pymongo.MongoClient(
    config('HOST')
)
mydb = client['Project_data']
collection = mydb["main_destination"]
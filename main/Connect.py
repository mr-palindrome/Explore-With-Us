import pymongo
import os
from decouple import config


client = pymongo.MongoClient(
    config('HOST')
)
mydb = client['Project_data']
collection_dest = mydb["main_destination"]
collection_sub = mydb["main_user_subs"]

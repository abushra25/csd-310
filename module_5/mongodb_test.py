##Created by Ahmed Bushra
##CYBR410-304J Data/Database Security 
##MongoDB test python file for Pytech



##Imports 
import pymongo
from pymongo import MongoClient

##Connecting to Ahmed's MongoDB
url = 'mongodb+srv://abushra:admin@cluster0.fgnygzs.mongodb.net/pytech?retryWrites=true&w=majority'

##Connecting to cluster
client = MongoClient(url)

##Pytech connection
db = client.pytech

##Output list of collections
print("\n-- Pytech COllection List --")
print(db.list_collection_names)

##Program end notification
input ("End of program, please press any key to exit...")

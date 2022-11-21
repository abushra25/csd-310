##Created by Ahmed Bushra
##CYBR410-304J Data/Database Security 
##MongoDB test python file for Pytech



##Imports 
from pymongo import MongoClient

##URL to connect to Ahmed's MongoDB
url = 'mongodb+srv://abushra:admin@cluster0.fgnygzs.mongodb.net/pytech?retryWrites=true&w=majority'

##Connecting to cluster
client = MongoClient(url)

##Pytech connection
db = client.pytech

collections = db.list_collection_names()

##Output list of collections
print("\n-- Pytech COllection List --")
print(collections)

##Program end notification
input ("\nEnd of program, please press any key to exit...")

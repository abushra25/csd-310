##pytech.queries to query student information
##Created by Ahmed Bushra
##CYBR410-304J Data/Database Security 

##Imports
import pymongo
from pymongo import MongoClient

##URL variable for MongoDB connection
url = "mongodb+srv://abushra:admin@cluster0.fgnygzs.mongodb.net/pytech?retryWrites=true&w=majority"

##Connections to DB and Pytech & Students collections
client = MongoClient(url)
db = client.pytech
students = db.students

##Output header message
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

##Data query output for all documents found in Students collection 
docs = students.find({})
for doc in docs:
    print("Student ID: " + doc ["Student_ID"] + "\nFirst Name: " + doc ["First_Name"] + "\nLast Name: " + doc ["Last_Name"])

##Data query output by Student_ID
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
doc = students.find_one({"Student_ID" : "1007"})
print("Student ID: " + doc ["Student_ID"] + "\nFirst Name: " + doc ["First_Name"] + "\nLast Name: " + doc ["Last_Name"])

##Program end message
input("\n End of program, press any key to continue...")
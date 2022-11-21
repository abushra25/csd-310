##pytech.insert to insert student information & output ID data
##Created by Ahmed Bushra
##CYBR410-304J Data/Database Security 

##Imports
import pymongo
from pymongo import MongoClient

##URL variable for MongoDB connection
url = "mongodb+srv://abushra:admin@cluster0.fgnygzs.mongodb.net/pytech?retryWrites=true&w=majority"

##Connections to cluster, pytech database, and students collection
client = MongoClient(url)
db = client.pytech

##Student data build

##Ahmed's data 
Ahmed = {
    "Student_ID": "1007",
    "First_Name": "Ahmed",
    "Last_Name": "Bushra",}

##Bilbo's data
Bilbo = {
    "Student_ID": "1008",
    "First_Name": "Bilbo",
    "Last_Name": "Baggins",}

##Frodo' data
Frodo = {
    "Student_ID": "1009",
    "First_Name": "Frodo",
    "Last_Name": "Baggins",}

##Retrieving students collection
students = db.students

##Insert statements + outputs. Stringing insert ID for output
print("\n  -- INSERT STATEMENTS --")
Ahmed_Student_ID = students.insert_one(Ahmed).inserted_id
print("Inserted student record Ahmed Bushra into the students collection with document_id" + str(Ahmed_Student_ID))

Bilbo_Student_ID = students.insert_one(Bilbo).inserted_id
print("Inserted student record Bilbo Baggins into the students collection with document_id" + str(Bilbo_Student_ID))

Frodo_Student_ID = students.insert_one(Frodo).inserted_id
print("Inserted student record Frodo Baggins into the students collection with document_id" + str(Frodo_Student_ID))

input("\nEnd of program, press any key to exit...")
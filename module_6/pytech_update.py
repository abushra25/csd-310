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

##Using Students collection to pull data
docs = students.find({})

##Output header message if current student documents
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

## Output of current documents in collection
for doc in docs:
    print("Student ID: " + doc["Student_ID"] + "\nFirst Name: " + doc["First_Name"] + "\nLast Name: " + doc["Last_Name"] + "\n")

##Updating Student_ID 1007 via update_one in 'students' collection
update_result = students.update_one({"Student_ID": "1007"}, {"$set": {"Last_Name": "Bushra II"}})

##find_one method to pull 1007 record
Ahmed = students.find_one({"Student_ID": "1007"})

##Output message for displaying 1007 document + output of updated record 
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

print("Student ID: " + Ahmed["Student_ID"] + "\nFirst Name: " + Ahmed["First_Name"] + "\nLast Name: " + Ahmed["Last_Name"] + "\n")

##End of program message 
input("\n\n  End of program, press any key to continue...")
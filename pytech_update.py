from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ttzvy81.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["students"]

result = db.students.update_one({"student_id": 1007}, {"$set": {"last_name": "Oakenshield II"}})

query = {"student_id": {"$gt": 1006}}
docs = db.students.find(query)

doc = db.students.find_one({"student_id": 1007})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x in docs:
    print("Student ID:", x["student_id"], "\nFirst Name:", x["first_name"], "\nLast Name:", x["last_name"], "\n")

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
print("Student ID:", doc["student_id"], "\nFirst Name:", doc["first_name"], "\nLast Name:", doc["last_name"], "\n")
print("")

input("End of program, press any key to continue...")

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ttzvy81.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["students"]

query = {"student_id": {"$gt": 1006}}
querys = {"student_id": {"$gt": 1006}}
docs = db.students.find(query)
docss = db.students.find(querys)

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x in docs:
    print("Student ID:", x["student_id"], "\nFirst Name:", x["first_name"], "\nLast Name:", x["last_name"], "\n")
print("-- INSERT STATEMENTS --")

john = {"student_id": 1010,
        "first_name": "John",
        "last_name": "Doe"}

john_student_id = students.insert_one(john).inserted_id

doc = db.students.find_one({"student_id": 1010})

print("Inserted student record into students collection with document_id", john_student_id, "\n")
print("-- DISPLAYING STUDENTS TEST DOC --")
print("Student ID:", doc["student_id"], "\nFirst Name:", doc["first_name"], "\nLast Name:", doc["last_name"], "\n")

queries = {"student_id": 1010}
db.students.delete_one(queries)

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x in docss:
    print("Student ID:", x["student_id"], "\nFirst Name:", x["first_name"], "\nLast Name:", x["last_name"], "\n")
print("")

input("End of program, press any key to continue...")

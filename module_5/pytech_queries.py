from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ttzvy81.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["students"]

query = {"student_id": {"$gt": 1006}}
docs = db.students.find(query)

doc = db.students.find_one({"student_id": 1008})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x in docs:
    print("Student ID:", x["student_id"], "\n", "First Name:", x["first_name"], "\n", "Last Name:", x["last_name"], "\n")

print("")
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
print("Student ID:", doc["student_id"])
print("First Name:", doc["first_name"])
print("Last Name:", doc["last_name"])
print("")
input("End of program, press any key to continue...")

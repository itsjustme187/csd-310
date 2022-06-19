from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ttzvy81.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["students"]
thorin = {"student_id": 1007,
             "first_name": "Thorin",
             "last_name": "Oakenshield"}
thorin_student_id = students.insert_one(thorin).inserted_id
bilbo = {"student_id": 1008,
            "first_name": "Bilbo",
            "last_name": "Baggins"}
bilbo_student_id = students.insert_one(bilbo).inserted_id
frodo={"student_id": 1009,
            "first_name": "Frodo",
            "last_name": "Baggins"}
frodo_student_id = students.insert_one(frodo).inserted_id
print("-- INSERT STATEMENTS --")
print(("Inserted student record Thorin Oakenshield in the students collection with document_id"),thorin_student_id)
print(("Inserted student record Bilbi Baggins in the students collection with document_id"),bilbo_student_id)
print(("Inserted student record Frodo Baggins in the students collection with document_id"),frodo_student_id)
print("")
input("End of program, press any key to exit...")

CREATE TABLE Student (
    student_id int NOT NULL AUTO_INCREMENT,
    first_name,
    last_name,
); 
CREATE TABLE Enrollment (
    term int,
    gpa int,
    start_date int,
    end_date int,
    team_id int,
); 
CREATE TABLE Course (
    course_id int,
    description,
    instructor int,
    grade int,
); 
MongoDB: find() Example 
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one() Example 
doc = db.collection_name.find_one({“student_id”: “1007”})
 
print(doc[“student_id”])

MongoDB: find() Example 
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one() Example 
doc = db.collection_name.find_one({“student_id”: “1008”})
 
print(doc[“student_id”])

MongoDB: find() Example 
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one() Example 
doc = db.collection_name.find_one({“student_id”: “1009”})
 
print(doc[“student_id”])
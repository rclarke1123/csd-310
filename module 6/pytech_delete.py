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
MongoDB: insert_one() Example 
fred = {
 “first_name”: “Fred”
}
fred_student_id = students.insert_one(fred).1007

print(fred_student_id)

Joe = {
 “first_name”: “Fred”
}
 Joe_student_id = students.insert_one(Joe).1008

print(Joe_student_id)

MongoDB: insert_one() Example
Bob = {
 “first_name”: “Bob”
}
 Bob_student_id = students.insert_one(Bob).1009

print(Bob_student_id)

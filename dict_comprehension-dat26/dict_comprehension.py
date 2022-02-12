# Create dict with students and it`s scores
from random import *
names = ["Alex", 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
# Generate random scores for students and check if they pass
student_score = {student.title(): randint(30, 100) for student in names}
print(f"The score which give a teacher for students: \n{student_score}")
passed_students = {students_pass: scores for (students_pass, scores) in student_score.items() if scores >= 60}
print(f"Students which pass:\n{passed_students}")
not_passed = {incomplete: score for incomplete, score in student_score.items() if score <= 60}
print(f"Students which not passed:\n{not_passed}")
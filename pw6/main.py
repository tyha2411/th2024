from input import InputManager
from domains.student import Student
from domains.course import Course
import os
import zlib
import pickle

def check_data_file():
    return os.path.exists("students.dat")

def decompress_data():
    with open("students.dat", "rb") as f:
        decompressed_data = zlib.decompress(f.read())

if check_data_file():
    decompress_data()

input_manager = InputManager()

num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    input_manager.input_student_info()

num_courses = int(input("Enter the number of courses: "))
for i in range(num_courses):
    input_manager.input_course()

input_manager.input_marks_for_all_courses()

with open("students.pkl", "wb") as f:
    pickle.dump(input_manager.students, f)

with open("courses.pkl", "wb") as f:
    pickle.dump(input_manager.courses, f)

with open("marks.pkl", "wb") as f:
    pickle.dump(input_manager.students, f)

compression_method = zlib.Z_BEST_COMPRESSION  
with open("students.dat", "wb") as f:
    with open("students.pkl", "rb") as f_students:
        with open("courses.pkl", "rb") as f_courses:
            with open("marks.pkl", "rb") as f_marks:
                f.write(zlib.compress(f_students.read() + f_courses.read() + f_marks.read(), compression_method))

input_manager.list_students()
input_manager.list_courses()
input_manager.list_marks()
input_manager.calculate_gpa()
input_manager.sort_students_by_gpa()
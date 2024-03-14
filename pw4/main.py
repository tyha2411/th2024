from input import InputManager
from domains.student import Student
from domains.course import Course

input_manager = InputManager()
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    input_manager.input_student_info()

num_courses = int(input("Enter the number of courses: "))
for i in range(num_courses):
    input_manager.input_course()

input_manager.input_marks_for_all_courses()
input_manager.list_students()
input_manager.list_courses()
input_manager.list_marks()
input_manager.calculate_gpa()
input_manager.sort_students_by_gpa()

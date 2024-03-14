import numpy as np
import math

class Student:
    def __init__(self, student_name, student_id, student_DOB):
        self.student_name = student_name
        self.student_id = student_id
        self.student_DOB = student_DOB
        self.courses = {}

    def __str__(self):
        return f"{self.student_name} (ID: {self.student_id}, DoB: {self.student_DOB})"

    def add_mark(self, course_name, mark):
        self.courses[course_name] = mark

    def calculate_gpa(self, course_credits):
        total_credits = sum(course_credits)
        total_points = sum([mark * credit for mark, credit in zip(self.courses.values(), course_credits)])
        gpa = total_points / total_credits
        return gpa

class Course:
    def __init__(self, course_name, course_id, credit):
        self.course_name = course_name
        self.course_id = course_id
        self.credit = credit

class InputManager:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_student_info(self):
        name = input("Enter Student name: ")
        student_id = input("Enter Student ID: ")
        dob = input("Enter Student date of birth (DD-MM-YYYY): ")
        self.students.append(Student(name, student_id, dob))

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student)

    def input_course(self):
        name = input("Enter course name: ")
        id2 = input("Enter course id: ")
        credit = float(input("Enter course credit: "))
        self.courses.append(Course(name, id2, credit))

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course.course_name)

    def input_marks_for_all_courses(self):
        course_credits = [course.credit for course in self.courses]
        for course in self.courses:
            print(f"Input marks for {course.course_name} ({course.course_id}):")
            for student in self.students:
                mark = float(input(f"Enter mark for {student.student_name}: "))
                mark = round(mark, 1)  
                mark = math.floor(mark)  
                student.add_mark(course.course_name, mark)

    def list_marks(self):
        print("List of Marks:")
        for student in self.students:
            print(f"{student.student_name}: {student.courses}")

    def calculate_gpa(self):
        course_credits = [course.credit for course in self.courses]
        for student in self.students:
            gpa = student.calculate_gpa(course_credits)
            print(f"{student.student_name}'s GPA: {gpa:.2f}")

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.calculate_gpa([course.credit for course in self.courses]), reverse=True)
        print("Sorted list of students by GPA descending:")
        for student in self.students:
            print(student)
            
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

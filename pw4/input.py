import math
from domains.student import Student
from domains.course import Course
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

   

   

class Students:
    def __init__(self, student_name, student_id, student_DOB):
        self.student_name = student_name
        self.student_id = student_id
        self.student_DOB = student_DOB

    def __str__(self):
        return f"{self.student_name} (ID: {self.student_id}, DoB: {self.student_DOB})"


class Courses:
    def __init__(self, course_name, course_id, students):
        self.course_name = course_name
        self.course_id = course_id
        self.student_marks = {student: 0 for student in students}

    def __str__(self):
        return f"{self.course_name} (ID: {self.course_id})"


class Other_Input:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_student_info(self):
        name = input("Enter Student name: ")
        student_id = input("Enter Student ID: ")
        dob = input("Enter Student date of birth (DD-MM-YYYY): ")
        self.students.append(Students(name, student_id, dob))

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student)

    def input_course(self):
        name = input("Enter course name: ")
        id2 = input("Enter course id: ")
        course = Courses(name, id2, self.students)
        self.courses.append(course)
        return course

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course)

    def input_marks_for_all_courses(self):
        for course in self.courses:
            print(f"Input marks for {course.course_name} ({course.course_id}):")
            for student in self.students:
                mark = input(f"Enter mark for {student.student_name}: ")
                course.student_marks[student] = float(mark)

    def list_marks(self):
        print("List of Marks:")
        for course in self.courses:
            print(f"{course.course_name} ({course.course_id}):")
            for student, mark in course.student_marks.items():
                print(f"{student.student_name}: {mark}")



input_manager = Other_Input()

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

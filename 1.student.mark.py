def input_student_info():
    return {'Name': input("Enter student name: "), 'Id': input("Enter student id: "), 'DOB': input("Enter student dob (DD-MM-YYYY): ")}

def list_students(students):
    print("List of Students:")
    [print(student) for student in students]

def input_course_info(number_of_students):
    return {'Course Name': input("Enter course name: "), 'Course Id': input("Enter course id: "), 'Student Mark': [0] * number_of_students}

def list_courses(courses):
    print("List of Courses:")
    [print(course) for course in courses]

def input_mark(students, courses):
    course_id = input("Enter course id: ")
    for i in range(len(students)):
        mark = float(input(f"Enter mark for student {students[i]['Name']}: "))
        courses[course_id]['Student Mark'][i] = mark

def list_marks(courses):
    print("List of Marks:")
    [print(f"{course['Course Name']} ({course['Course Id']}): {course['Student Mark']}") for course in courses]

number_of_students = int(input("Enter the number of students: "))
student_array = [input_student_info() for _ in range(number_of_students)]

number_of_courses = int(input("Enter the number of courses: "))
course_array = {input_course_info(number_of_students)['Course Id']: input_course_info(number_of_students) for _ in range(number_of_courses)}

while True:
    print("\nOptions:")
    print("1. Info Students")
    print("2. Info Courses")
    print("3. Marks")
    print("4. List Marks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        list_students(student_array)
    elif choice == '2':
        list_courses(course_array.values())
    elif choice == '3':
        input_mark(student_array, course_array)
    elif choice == '4':
        list_marks(course_array.values())
    elif choice == '5':
        break
    else:
        print("Please try again.")

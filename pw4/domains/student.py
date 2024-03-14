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
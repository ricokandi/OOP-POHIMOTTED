"""School class which stores information about courses and students."""
import random


class School
"""School class."""

    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        id = random.randint(1, 10000)
        for school_student in self.students:
            if school_student.id == id:
                id = random.randint(0, 10000)
        if student not in self.students:
            student.set_id(id)
            self.students.append(student)

    def get_students(self):
        return self.students

    def add_student_grade(self, student, course, grade: int):
        if student in self.students and course in self.courses:
            student.set_grade(course, grade)
            course.set_grade(student, grade)

    def get_courses(self):
        return self.courses

    def get_students_ordered_by_average_grade(self):
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)
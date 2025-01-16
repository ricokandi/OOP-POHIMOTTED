"""Student class with student name and grades."""


class Student:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.grades = []

    def set_id(self, id: int):
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        return self.id

    def set_grade(self, course, grade):
        self.grades.append((course, grade))

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        average_grade = -1
        if len(self.grades) == 0:
            return average_grade
        else:
            sum_of_grades = 0
            for grade in self.grades:
                sum_of_grades += grade[1]
            average_grade = sum_of_grades / len(self.grades)
        return average_grade

    def __repr__(self) -> str:
        return self.name

"""Course class with name and grades."""


class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

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

    def __repr__(self):
        return self.name

    def set_grade(self, student, grade):
        self.grades.append((student, grade))

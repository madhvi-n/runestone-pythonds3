"""
Class hierarchy for types of people in college campus
"""

class College:
    def __init__(self, college):
        self.college = college

    def __str__(self):
        return f"College: {self.college}"


class Department(College):
    def __init__(self, college, department, **kwargs):
        self.department = department
        super().__init__(college, **kwargs)

    def __str__(self):
        return f"Department of {self.department}"

    def current_department(self):
        return f"Department of {self.department}"


class Professor(Department):
    def __init__(self, college, department, name, age, **kwargs):
        super().__init__(college, department)
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} in {self.department} department"

    def age(self):
        return f"{self.age}"


class Student(Department):
    def __init__(self, college, department, student_name, student_age, **kwargs):
        super().__init__(college, department)
        self.student_name = student_name
        self.student_age = student_age

    def __str__(self):
        return f"{self.student_name} from {super().current_department()}"


def main():
    professor = Professor('Rice University', 'Arts', 'Ana Mathew', 36)
    print(professor)
    print(professor.current_department())

    student = ('Rice University', 'Computer Science', 'Jane Doe', 22)
    print(student)


if __name__ == '__main__':
    main()

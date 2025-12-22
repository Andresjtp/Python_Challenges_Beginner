class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average(self):
        if not self.grades:
            return 0
        sum_grades = 0
        for subject, grades in self.grades.items():
            sum_grades += grades
        average = sum_grades / len(self.grades)
        print(f"average grade: {average}")
        return average

    def letter_grade(self):
        avg = self.average()
        if avg >= 90:
            letter_grade = "A"
        elif avg >= 80:
            letter_grade = "B"
        elif avg >= 70:
            letter_grade = "C"
        elif avg >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
        print(f"Letter grade: {letter_grade}")
        return letter_grade

    def student_result(self):
        for subjects, grades in self.grades.items():
            if grades >= 70:
                print(f"{self.name} passed {subjects}!")
            else:
                print(f"{self.name} failed {subjects} :(")

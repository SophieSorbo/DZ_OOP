class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = [i for student_grades in self.grades.values() for i in student_grades]
        result = sum(all_grades) / len(all_grades) if all_grades else 0.0
        return f"{result:.1f}"

    def __lt__(self, student):
        if not isinstance(student, Student):
            return f'Такого студента нет'
        else:
            if self.average_grade() < student.average_grade():
                return f'У {student.name} {student.surname} оценки лучше чем у {self.name} {self.surname}'
            else:
                return f'У {self.name} {self.surname} оценки лучше чем у {student.name} {student.surname}'

    def average_grade_all(self, course):
        aver_grade = []
        for student in self:
            if isinstance(student, Student) and course in student.courses_in_progress:
                for theme, grade in student.grades.items():
                    if theme == course:
                        aver_grade.extend(grade)
        result = sum(aver_grade) / len(aver_grade) if aver_grade else 0.0
        return f"Средняя оценка за домашние задания по курсу {course}: {result:.1f}"

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_grade()}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = [i for student_grades in self.grades.values() for i in student_grades]
        result = sum(all_grades) / len(all_grades) if all_grades else 0.0
        return f"{result:.1f}"

    def average_grade_all(self, course):
        aver_grade = []
        for lecturer in self:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
                for theme, grade in lecturer.grades.items():
                    if theme == course:
                        aver_grade.extend(grade)
        result = sum(aver_grade) / len(aver_grade) if aver_grade else 0.0
        return f"Средняя оценка за лекции по курсу {course}: {result:.1f}"

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            return f'Такого лектора нет'
        else:
            if self.average_grade() < lecturer.average_grade():
                return f'У {lecturer.name} {lecturer.surname} оценки лучше чем у {self.name} {self.surname}'
            else:
                return f'У {self.name} {self.surname} оценки лучше чем у {lecturer.name} {lecturer.surname}'



    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_grade()}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'C++']
student_2 = Student('John', 'Doe', 'male')
student_2.courses_in_progress += ['Python', 'C++']
mentor_1 = Reviewer('Renny', 'Gooder')
mentor_1.courses_attached += ['Python']
mentor_2 = Reviewer('Some', 'Buddy')
mentor_2.courses_attached += ['C++']

mentor_1.rate_hw(student_1, 'Python', 9)
mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'Python', 10)

mentor_1.rate_hw(student_2, 'Python', 7)
mentor_1.rate_hw(student_2, 'Python', 8)
mentor_1.rate_hw(student_2, 'Python', 6)

mentor_2.rate_hw(student_1, 'C++', 10)
mentor_2.rate_hw(student_1, 'C++', 8)
mentor_2.rate_hw(student_1, 'C++', 6)

mentor_2.rate_hw(student_2, 'C++', 7)
mentor_2.rate_hw(student_2, 'C++', 8)
mentor_2.rate_hw(student_2, 'C++', 9)


lector_1 = Lecturer('John', 'Jones')
lector_1.courses_attached += ['Python']
student_1.rate_hw(lector_1, 'Python', 10)
student_1.rate_hw(lector_1, 'Python', 8)
student_2.rate_hw(lector_1, 'Python', 9)
student_2.rate_hw(lector_1, 'Python', 10)


lector_2 = Lecturer('Alex', 'Divon')
lector_2.courses_attached += ['C++']
student_1.rate_hw(lector_2, 'C++', 9)
student_1.rate_hw(lector_2, 'C++', 8)
student_2.rate_hw(lector_2, 'C++', 9)
student_2.rate_hw(lector_2, 'C++', 10)


compare = student_1.__lt__(student_2)
compare_lectors = lector_1.__lt__(lector_2)

aver_grade_st = Student.average_grade_all([student_1, student_2], 'Python')
aver_grade_lect = Lecturer.average_grade_all([lector_1, lector_2], 'Python')

print()
print(aver_grade_st, end='\n\n')
print(aver_grade_lect, end='\n\n')
print(compare_lectors, end='\n\n')
print(compare, end='\n\n')
print(student_1, end='\n\n')
print(student_2, end='\n\n')
print(lector_1, end='\n\n')
print(lector_2, end='\n\n')
print(mentor_1, end='\n\n')
print(mentor_2, end='\n\n')
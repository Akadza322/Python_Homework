class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mean_grades = float()

    def course_rate(self, lecturer, course, grade):
        if lecturer.courses_attached == self.finished_courses or self.courses_in_progress:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = (f"Имя: {self.name}"
                  f"\nФамилия: {self.surname}"
                  f"\nСредняя оценка за домашние задания: {self.mean_grades}"
                  f"\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}"
                  f"\nЗавершенные курсы: {",".join(self.finished_courses)}")
        return result

    def arithmetic_mean(self, student):
        for count in student.grades:
            self.mean_grades += sum(self.grades[count])
        self.mean_grades /= len(self.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        result = (f"Имя: {self.name}"
                  f"\nФамилия: {self.surname}")
        return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}
        self.mean_grades = float()

    def __str__(self):
        result = (f"Имя: {self.name}"
                  f"\nФамилия: {self.surname}"
                  f"\nСредняя оценка за лекцию: {self.mean_grades}")
        return result

    def arithmetic_mean(self, lecturer):
        for count in lecturer.course_grades:
            self.mean_grades += sum(lecturer.course_grades[count]) / len(lecturer.course_grades[count])


best_student_1 = Student('Roy', 'Eman', 'your_gender')
best_student_2 = Student('Ivan', 'Ivanov', 'your_gender')
best_student_1.courses_in_progress += ['Git', 'Python']
best_student_1.finished_courses += ['Введение в программирование']
best_student_2.courses_in_progress += ['Python', 'Git']
best_student_2.finished_courses += ['Введение в программирование']

reviewer_mentor_1 = Reviewer('Some', 'Buddy')
reviewer_mentor_1.courses_attached += ['Python']
reviewer_mentor_2 = Reviewer('Jon', 'Jons')
reviewer_mentor_2.courses_attached += ['Git']

lecturer_mentor_1 = Lecturer('Roy', 'Jons')
lecturer_mentor_1.courses_attached += ['Введение в программирование']
lecturer_mentor_2 = Lecturer('Stepan', 'Abramov')
lecturer_mentor_2.courses_attached += ['Python']

reviewer_mentor_1.rate_hw(best_student_1, 'Python', 10)
reviewer_mentor_1.rate_hw(best_student_2, 'Python', 8)
reviewer_mentor_2.rate_hw(best_student_1, 'Git', 10)
reviewer_mentor_2.rate_hw(best_student_2, 'Git', 9)

best_student_1.course_rate(lecturer_mentor_1, 'Введение в программирование', 10)
best_student_2.course_rate(lecturer_mentor_1, 'Введение в программирование', 9)
best_student_1.course_rate(lecturer_mentor_2, 'Python', 10)
best_student_2.course_rate(lecturer_mentor_2, 'Python', 7)

lecturer_mentor_1.arithmetic_mean(lecturer_mentor_1)
lecturer_mentor_2.arithmetic_mean(lecturer_mentor_2)

best_student_1.arithmetic_mean(best_student_1)
best_student_2.arithmetic_mean(best_student_2)


print(lecturer_mentor_1.course_grades)
print(lecturer_mentor_2.course_grades)
print()
print(f'{best_student_1}\n\n{best_student_2}')
print()
print(f'{reviewer_mentor_1}\n\n{reviewer_mentor_2}')
print()
print(f'{lecturer_mentor_1}\n\n{lecturer_mentor_2}')
print()

if lecturer_mentor_1.mean_grades > lecturer_mentor_2.mean_grades:
    print(f'Лектор с наивысшим-средним баллом:\n'
          f'{lecturer_mentor_1}')
else:
    print(f'{lecturer_mentor_2}')

print()

if best_student_1.mean_grades > best_student_2.mean_grades:
    print(f'Студент с наивысшим-средним баллом:\n'
          f'{best_student_1}')
else:
    print(f'{best_student_2}')

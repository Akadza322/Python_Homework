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
        for course in student.grades:
            if course in self.grades:
                self.mean_grades += sum(student.grades[course]) / len(student.grades[course])
        self.mean_grades /= len(student.grades)

    def __eq__(self, other):
        return self.mean_grades == best_student_1.mean_grades

    def __gt__(self, other):
        return self.mean_grades > best_student_1.mean_grades

    def __lt__(self, other):
        return self.mean_grades < best_student_1.mean_grades


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

    def __eq__(self, other):
        return self.mean_grades == lecturer_mentor_1.mean_grades

    def __gt__(self, other):
        return self.mean_grades > lecturer_mentor_1.mean_grades

    def __lt__(self, other):
        return self.mean_grades < lecturer_mentor_1.mean_grades


def ar_student(student_list, courses):
    acg = {}
    for student in student_list:
        if isinstance(student, Student):
            for course in courses:
                if course in acg:
                    for count in student.grades:
                        if count == course:
                            acg[course] += student.grades[course]
                else:
                    for count in student.grades:
                        if count == course:
                            acg[course] = student.grades[course]
    for key, value in acg.items():
        acg[key] = sum(value) / len(value)
    return acg


def ar_lecturer(lecturer_list, courses):
    agfl = {}
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer):
            for course in courses:
                if course in agfl:
                    for count in lecturer.course_grades:
                        if count == course:
                            agfl[course] += lecturer.course_grades[course]
                else:
                    for count in lecturer.course_grades:
                        if count == course:
                            agfl[course] = lecturer.course_grades[course]
    for key, value in agfl.items():
        agfl[key] = sum(value) / len(value)
    return agfl


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

reviewer_mentor_1.rate_hw(best_student_1, 'Python', 1)
reviewer_mentor_1.rate_hw(best_student_1, 'Python', 2)
reviewer_mentor_1.rate_hw(best_student_2, 'Python', 3)
reviewer_mentor_1.rate_hw(best_student_2, 'Python', 4)
reviewer_mentor_2.rate_hw(best_student_1, 'Git', 5)
reviewer_mentor_2.rate_hw(best_student_1, 'Git', 6)
reviewer_mentor_2.rate_hw(best_student_2, 'Git', 7)
reviewer_mentor_2.rate_hw(best_student_2, 'Git', 8)

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
print(ar_student([best_student_1, best_student_2], ['Python', 'Git']))
print()
print(ar_lecturer([lecturer_mentor_1, lecturer_mentor_2], ['Введение в программирование', 'Python']))

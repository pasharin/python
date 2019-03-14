# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)

    def area(self):
        self.perimetr /=2
        self.area =  round(math.sqrt(self.perimetr*(self.perimetr - self.AB)*(self.perimetr - self.BC)* (self.perimetr - self.CA)),2)
        return (self.area)

    def height(self):
        self.area *=2
        self.height =  round((self.area / self.CA),2)
        return (self.height)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

my_tri = Triangle(2,5,6,9,9,6)


print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC,my_tri.CA))
print('Периметр треугольника АВС равен {}'.format(my_tri.perimetr()))
print('Площадь треугольника АВС равна {}'.format(my_tri.area()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_tri.height()))

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random

class School:
    def __init__(self, school_name, school_adress, teachers, students):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents

                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                    }

    @property
    def name(self):
        return 'School name ' \
               '"{}"'.format(self._school_name)

    @property
    def adress(self):
        return '{}'.format(self._school_adress)


class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    @property
    def get_full_name(self):
        return '{0} {1} {2}'.format(self._last_name,
                                    self._first_name,
                                    self._middle_name)

    @property
    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self._last_name,
                                     self._first_name[:1],
                                     self._middle_name[:1])


class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mather, father):
        People.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mather': mather,
            'father': father
            }

    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parents(self):
        return self._parents


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name,
                 courses, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes


teachers = [
    Teacher('Izmailov', 'Leonid', 'Andreevich', 'Math',
            ['1A', '2B', '1C']),
    Teacher('Belkin', 'Viktor', 'Vadimovich', 'Biology',
            ['1A', '2B', '1C'])]


students = [
    Student('Bil', 'Big', 'Boss', '1A', 'Bil О. А.', 'Bil А. В.'),
    Student('Patter', 'pa', 'Ki', '2B', 'patter Т.В.', 'Patter А.В.'),
    Student('Mor', 'Mar', 'Mir', '1C', 'Mor А.E.', 'Mor С.А.'),
    Student('Mass', 'Oss', 'Iss', '1A', 'Mass А.К.', 'Mass Н.В.'),
    Student('Bob', 'Arr', 'Ass', '1C', 'Bob В.А.', 'Bob А.Т'),
    Student('Ivanov', 'Serg', 'Serg', '2B', 'Ivanova Н.А.', 'Ivanov Н.С.')]

school = School('Hight School', 'Moscow', teachers, students)

print(school.name)
print(school.adress)

print('\nClasses list:')
print(', '.join(school.get_all_classes()))

print('\nList "1A" class:')
print('\n'.join(school.get_students('1A')))

print('\nList "1C" class:')
print('\n'.join(school.get_students('1C')))

print('\nList "2B" class:')
print('\n'.join(school.get_students('2B')))


student = school.find_student('Ivanov Serg Serg')
print('\nStudent: {0}\nClass: "{1}"\n''Teacher: {2}\nSubject: {3}'.format(student['full_name'],
student['class_room'], ', '.join(student['teachers']), ', '.join(student['lessons'])))

print('Parents: {0}, {1}'.format(student['parents']['mather'], student['parents']['father']))

print('\nClass: "1C"\nTeacher: ''{0}'.format(', '.join(school.get_teachers('c1'))))













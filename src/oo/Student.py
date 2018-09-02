#! /usr/bin/python3
# -*-coding:UTF-8-*-


class Student(object):
    gender = 'Male'

    __grade = 6

    def __init__(self):
        self.name = 'unknown'

    def __init__(self, name):
        self.name = name
        self.__age = 20
        self.gender = 'Female'

    def desc(self):
        print('my name is %s, I am %d years old.' % (self.name, self.__age))

    def play(self):
        print('this is %s playing' % self.name)


class SeniorStudent(Student):

    def __init__(self, name):
        Student.__init__(self, name)

    def desc(self):
        Student.desc(self)
        print('This is senior student %s, gender is %s' % (self.name, self.gender))

    def play(self):
        print('this is senior student %s playing' % self.name)


def play(stu):
    stu.play()

xiaoming = Student('xiaoming')
print(xiaoming.name)
print(xiaoming.gender)
xiaoming.desc()

xiaohong = SeniorStudent('xiaohong')
xiaohong.desc()
xiaohong.play()

print('is xiaoming senior ?', isinstance(xiaoming, SeniorStudent))
print('is xiaoming student ?', isinstance(xiaoming, Student))
print('is xiaohong senior ?', isinstance(xiaohong, SeniorStudent))
print('is xiaohong student ?', isinstance(xiaohong, Student))

play(xiaoming)
play(xiaohong)

from abc import ABC, abstractmethod
from datetime import date
from university import University
from exceptions import ConstError
import random
import weakref


class Person(ABC):
    @abstractmethod
    def __init__(self, first_name, last_name, birthday, gender):
        self.__birthday = birthday
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender

    def get_age(self):
        # Every year has 365.2425 days
        days = (date.today() - self.__birthday) / 365.2425
        return days.days


class Student(Person):
    __listOfNums = []
    validDegrees = ["Bachelor", "Master", "Doctoral"]

    def __init__(
        self,
        first_name,
        last_name,
        birthday,
        gender,
        faculty,
        academic_degree,
        university,
        gpa=15,
    ):
        super().__init__(first_name, last_name, birthday, gender)

        if academic_degree in Student.validDegrees:
            self.__academic_degree = academic_degree
        else:
            raise ValueError("Academic degree is invalid.")

        if faculty == None:
            self.faculty = None
        else:
            self.faculty = weakref.ref(faculty)
        self.university = weakref.proxy(university)
        self.gpa = gpa
        rand = random.randint(100000, 999999)
        while rand in Student.__listOfNums:
            rand = random.randint(100000, 999999)
        self.__std_num = rand
        Student.__listOfNums.append(rand)
        University.std_nums[self.university].append(rand)

    def __str__(self):
        return f"I am {self.first_name} {self.last_name} and studying at {self.university.name}"

    @property
    # Getter method
    def std_num(self):
        return self.__std_num

    # Setter method
    @std_num.setter
    def std_num(self, val):
        raise ConstError("Student number is immutable.")

    @property
    # Getter method
    def academic_degree(self):
        return self.__academic_degree

    # Setter method
    @academic_degree.setter
    def academic_degree(self, val):
        if val in Student.validDegrees:
            self.__academic_degree = val
        else:
            raise ValueError("Academic degree is invalid.")


class Professor(Person):
    validRanks = [
        "Professor",
        "Associate Professor",
        "Assistant Professor",
        "Lecturer",
    ]

    def __init__(
        self,
        first_name,
        last_name,
        birthday,
        gender,
        faculty,
        academic_rank,
        university,
        salary,
    ):
        super().__init__(first_name, last_name, birthday, gender)

        if academic_rank in Professor.validRanks:
            self.__academic_rank = academic_rank
        else:
            raise ValueError("Academic rank is invalid.")
        if faculty == None:
            self.faculty = None
        else:
            self.faculty = weakref.ref(faculty)
        self.university = university
        self._salary = salary

    def __str__(self):
        return f"I am {self.academic_rank} {self.first_name} {self.last_name} and studying at {self.university.name}"

    @property
    # Getter method
    def academic_rank(self):
        return self.__academic_rank

    # Setter method
    @academic_rank.setter
    def academic_rank(self, val):
        if val in Professor.validRanks:
            self.__academic_rank = val
        else:
            raise ValueError("Academic rank is invalid.")

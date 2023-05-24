import weakref
import person


class University:
    std_nums = dict()
    ALL_INSTANCES = list()

    def __init__(
        self,
        filename=None,
        name=None,
        established=None,
        chancellor=None,
        faculties=None,
    ):
        if filename == None:
            self.name = name
            self.established = established
            self.chancellor = chancellor
            self.faculties = faculties
        else:
            f = open(filename)
            l = [i for i in f.read().split(" - ")]
            self.name, self.established, self.chancellor = l
            f.close()
            self.faculties = []
        University.ALL_INSTANCES.append(self.name)
        self.wr = weakref.ref(self)
        if len(University.ALL_INSTANCES) == 4:
            raise RuntimeError("More than 3 universities.")
        University.std_nums[self.wr] = []

    def __del__(self):
        if self.name in University.ALL_INSTANCES:
            University.ALL_INSTANCES.remove(self.name)

    def __str__(self):
        return f"Here is {self.name}."

    def add_faculties(self, *args):
        for item in args:
            self.faculties.append(item)

    @classmethod
    def which_university_is_this(cls, std_num):
        for item in University.std_nums:
            if std_num in University.std_nums[item]:
                return item()
        return None


class Faculty:
    def __init__(self, name, university, students=tuple(), professors=[]):
        self.name = name
        self.university = weakref.ref(university)
        self.students = students
        self.professors = professors
        for item in professors:
            item.faculty = weakref.proxy(self)

    def __str__(self):
        return f"Here is {self.name}."

    def add_students(self, *args):
        self.students = self.students + args

    def add_professors(self, *args):
        self.professors = self.professors + list(args)

    def get_top_remain(self, degree):
        std_list = [
            student for student in self.students if student.academic_degree == degree
        ]
        std_list.sort(key=lambda x: x.gpa, reverse=True)
        return iter(std_list)

    def __iadd__(self, other):
        if isinstance(other, Faculty):
            for item in other.professors:
                self.add_professors(item)
            return self
        elif isinstance(other, person.Professor):
            self.add_professors(other)
            return self

    def __mod__(self, n):
        return filter(lambda student: student.gpa >= n, self.students)

    def __contains__(self, person):
        return person in self.students or person in self.professors

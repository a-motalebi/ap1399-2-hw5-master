from time import time
from datetime import date
from person import Student


def hack_salary(professor_obj):
    return professor_obj._salary


class Timer:
    def __enter__(self):
        self.t1 = time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.total = time() - self.t1


def read_data(university, faculty, filename):
    f = open(filename)
    informations = [i.split(", ") for i in f.read().split(" \n") if len(i) != 0]
    f.close()
    for item in informations:
        item[2] = item[2].split("-")
    for data in informations:
        if len(data) == 5:
            faculty.add_students(
                Student(
                    data[0],
                    data[1],
                    date(int(data[2][0]), int(data[2][1]), int(data[2][2])),
                    data[3],
                    faculty,
                    data[4],
                    university,
                )
            )
        if len(data) == 6:
            faculty.add_students(
                Student(
                    data[0],
                    data[1],
                    date(int(data[2][0]), int(data[2][1]), int(data[2][2])),
                    data[3],
                    faculty,
                    data[4],
                    university,
                    float(data[5]),
                )
            )

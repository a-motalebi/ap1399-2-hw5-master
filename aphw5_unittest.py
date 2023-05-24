import unittest
from datetime import date
from person import Person, Student, Professor
from aphw5 import Timer, hack_salary, read_data
from university import University, Faculty
from exceptions import ConstError


class Test(unittest.TestCase):

    ## ---------------- Person Test - 1 Test ----------------
    def test_person(self):
        with self.assertRaises(TypeError):
            p = Person("Mohammad Mahdi", "Shojaefar", date(1999, 8, 29), "Male")

    ## ---------------- Student Tests - 4 Tests ----------------
    def test_student_diffrent_stdnum(self):
        # only before running this test, change your code such that std num be 1,2 or 3.
        # explain what we should do to checking this test.
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        s1 = Student(
            "Mohammad Mahdi",
            "Shojaefar",
            date(1999, 8, 29),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            16,
        )

        s2 = Student(
            "Amirreza",
            "Sefidchian",
            date(1999, 2, 11),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            17,
        )

        s3 = Student(
            "Mohammad Hossein",
            "Amini",
            date(1997, 1, 1),
            "Male",
            ee,
            "Master",
            amirkabir,
            18,
        )

        self.assertFalse(
            s1.std_num == s2.std_num
            or s1.std_num == s3.std_num
            or s2.std_num == s3.std_num
        )

    def test_student_stdnum(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        s1 = Student(
            "Mohammad Mahdi",
            "Shojaefar",
            date(1999, 8, 29),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            12,
        )
        print(f"{s1.first_name}'s student number is {s1.std_num}")
        self.assertEqual(True, 100000 < s1.std_num < 999999)
        with self.assertRaises(ConstError):
            s1.std_num = 123456

    def test_student_age(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        s1 = Student(
            "Mohammad Mahdi",
            "Shojaefar",
            date(1999, 8, 29),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            12,
        )
        s2 = Student(
            "Amirreza",
            "Sefidchian",
            date(1999, 2, 11),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            12.1,
        )
        self.assertEqual(s2.get_age(), 22)
        self.assertGreater(s2.get_age(), s1.get_age())
        print(s2)

    def test_student_academic_degree(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        with self.assertRaises(ValueError):
            s1 = Student(
                "Mohammad Mahdi",
                "Shojaefar",
                date(1999, 8, 29),
                "Male",
                ee,
                "Diploma",
                amirkabir,
                12,
            )
        s2 = Student(
            "Mohammad Hossein",
            "Amini",
            date(1960, 1, 1),
            "Male",
            ee,
            "Master",
            amirkabir,
            16,
        )
        with self.assertRaises(ValueError):
            s2.academic_degree = "Diploma"
        self.assertEqual(s2.academic_degree, "Master")

    # ---------------- Professor Tests - 3 Tests ----------------
    def test_professor_academic_rank(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        with self.assertRaises(ValueError):
            p1 = Professor(
                "Amir",
                "Jahanshahi",
                date(1980, 1, 1),
                "Male",
                ee,
                "Doctor",
                amirkabir,
                1000000,
            )
        p2 = Professor(
            "Reza",
            "Sarraf Shirazi",
            date(1960, 1, 1),
            "Male",
            ee,
            "Associate Professor",
            amirkabir,
            1100000,
        )
        with self.assertRaises(ValueError):
            p2.academic_rank = "Doctor"
        self.assertEqual(p2.academic_rank, "Associate Professor")

    def test_professor_salary(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        p = Professor(
            "Reza",
            "Sarraf Shirazi",
            date(1960, 1, 1),
            "Male",
            ee,
            "Associate Professor",
            amirkabir,
            1100000,
        )
        with self.assertRaises(AttributeError):
            print(p.salary)

    def test_professor_hack_salary(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        p = Professor(
            "Reza",
            "Sarraf Shirazi",
            date(1960, 1, 1),
            "Male",
            ee,
            "Associate Professor",
            amirkabir,
            1100000,
        )
        self.assertEqual(hack_salary(p), 1100000)

    # ---------------- University Tests - 4 Tests ----------------
    def test_university_constructor1(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        tehran = University(
            chancellor="Mahmoud Nili Ahmadabadi",
            name="University of Tehran",
            established=1934,
        )

        self.assertEqual(
            True,
            amirkabir.chancellor == "Seyed Ahmad Motamedi"
            and tehran.chancellor == "Mahmoud Nili Ahmadabadi",
        )

        self.assertEqual(
            True,
            amirkabir.established == 1928
            and amirkabir.name == "Amirkabir University of Technology",
        )

        self.assertEqual(
            True, tehran.established == 1934 and tehran.name == "University of Tehran"
        )

    def test_university_constructor2(self):
        amirkabir = University(filename="test_university_constructor2.txt")
        ce = Faculty("Computer Engineering", amirkabir)
        ee = Faculty("Electrical Engineering", amirkabir)
        self.assertEqual(amirkabir.name, "Amirkabir University of Technology")
        amirkabir.add_faculties(ee, ce)
        self.assertIn(ee, amirkabir.faculties)
        self.assertIn(ce, amirkabir.faculties)
        self.assertIn(
            amirkabir.faculties[0].name,
            ["Computer Engineering", "Electrical Engineering"],
        )

    def test_university_which_university(self):
        print(University.ALL_INSTANCES)
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        tehran = University(
            chancellor="Mahmoud Nili Ahmadabadi",
            name="University of Tehran",
            established=1934,
        )
        ce = Faculty("Computer Engineering", amirkabir)
        ee = Faculty("Electrical Engineering", tehran)
        s1 = Student(
            "Mohammad Mahdi",
            "Shojaefar",
            date(1999, 8, 29),
            "Male",
            ce,
            "Bachelor",
            amirkabir,
        )
        self.assertEqual(University.which_university_is_this(s1.std_num), amirkabir)
        self.assertEqual(University.which_university_is_this(1234567), None)

    def test_university_limit(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )

        tehran = University(
            chancellor="Mahmoud Nili Ahmadabadi",
            name="University of Tehran",
            established=1934,
        )
        sharif = University(
            established=1966,
            chancellor="Mahmoud Fotouhi Firouzabad",
            name="Sharif University of Technology",
        )
        with self.assertRaises(RuntimeError):
            yazd = University(
                established=1989,
                chancellor="Qasem BoridLoghmani",
                name="Yazd University",
            )

    ## ---------------- Faculty Tests - 5 Tests ----------------
    def test_faculty_constructor(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        p1 = Professor(
            "Amir",
            "Jahanshahi",
            date(1980, 1, 1),
            "Male",
            None,
            "Assistant Professor",
            amirkabir,
            1000000,
        )
        p2 = Professor(
            "Reza",
            "Sarraf Shirazi",
            date(1960, 1, 1),
            "Male",
            None,
            "Associate Professor",
            amirkabir,
            1100000,
        )
        ee = Faculty("Electrical Engineering", amirkabir, professors=[p1, p2])
        self.assertEqual(p1.faculty, ee)
        self.assertEqual(ee.professors, [p1, p2])
        ce = Faculty("Computer Engineering", amirkabir)
        self.assertEqual(ce.professors, [])

    def test_faculty_add_methods(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        p1 = Professor(
            "Amir",
            "Jahanshahi",
            date(1980, 1, 1),
            "Male",
            ee,
            "Assistant Professor",
            amirkabir,
            1000000,
        )
        s1 = Student(
            "Mohammad Mahdi",
            "Shojaefar",
            date(1999, 8, 29),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            12,
        )
        s2 = Student(
            "Amirreza",
            "Sefidchian",
            date(1999, 2, 11),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            12.1,
        )
        s3 = Student(
            "Mohammad Hossein",
            "Amini",
            date(1997, 1, 1),
            "Male",
            ee,
            "Master",
            amirkabir,
            12.2,
        )
        ee.add_professors(p1)
        ee.add_students(s1, s2, s3)
        self.assertEqual(ee.professors, [p1])
        self.assertEqual(
            True, s1 in ee.students and s2 in ee.students and s3 in ee.students
        )

    def test_faculty_get_top(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        s1 = Student(
            "Mohammad Mahdi",
            "Shojaefar",
            date(1999, 8, 29),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            12,
        )
        s2 = Student(
            "Amirreza",
            "Sefidchian",
            date(1999, 2, 11),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            12.3,
        )
        s3 = Student(
            "Mohammad Hossein",
            "Amini",
            date(1997, 1, 1),
            "Male",
            ee,
            "Master",
            amirkabir,
            12.2,
        )
        s4 = Student(
            "Amir Hassan",
            "Ashnaee",
            date(1994, 1, 1),
            "Male",
            ee,
            "Doctoral",
            amirkabir,
            12.4,
        )
        ee.add_students(s1, s2, s3, s4)
        print()
        bh = ee.get_top_remain("Bachelor")
        ms = ee.get_top_remain("Master")
        self.assertEqual(True, next(bh) == s2)
        self.assertEqual(True, next(ms) == s3)
        self.assertEqual(True, next(bh) == s1)

    def test_faculty_operator_add(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ce = Faculty("Computer Engineering", amirkabir)
        ee = Faculty("Electrical Engineering", amirkabir)
        p1 = Professor(
            "Amir",
            "Jahanshahi",
            date(1980, 1, 1),
            "Male",
            ce,
            "Assistant Professor",
            amirkabir,
            1000000,
        )
        p3 = Professor(
            "Iman",
            "Shraifi",
            date(1970, 1, 1),
            "Male",
            ee,
            "Assistant Professor",
            amirkabir,
            105000,
        )
        p2 = Professor(
            "Reza",
            "Sarraf Shirazi",
            date(1960, 1, 1),
            "Male",
            ee,
            "Associate Professor",
            amirkabir,
            1100000,
        )
        p4 = Professor(
            "Mehrdad",
            "Abedi",
            date(1950, 1, 1),
            "Male",
            ee,
            "Professor",
            amirkabir,
            1200000,
        )
        ce += p1
        ee += p2
        ee += p3
        ee += p4
        self.assertIn(p1, ce.professors)
        self.assertIn(p2, ee.professors)
        self.assertIn(p3, ee.professors)
        self.assertIn(p4, ee.professors)
        ee += ce
        self.assertIn(p1, ee.professors)
        self.assertIn(p1, ce.professors)
        self.assertEqual(4, len(ee.professors))
        self.assertEqual(1, len(ce.professors))
        self.assertEqual(ee.name, "Electrical Engineering")

    def test_faculty_other_operators(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        s1 = Student(
            "Mohammad Mahdi",
            "Shojaefar",
            date(1999, 8, 29),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            16,
        )

        s2 = Student(
            "Amirreza",
            "Sefidchian",
            date(1999, 2, 11),
            "Male",
            ee,
            "Bachelor",
            amirkabir,
            17,
        )
        s3 = Student(
            "Mohammad Hossein",
            "Amini",
            date(1997, 1, 1),
            "Male",
            ee,
            "Master",
            amirkabir,
            18,
        )
        s4 = Student(
            "Amir Hassan",
            "Ashnaee",
            date(1994, 1, 1),
            "Male",
            ee,
            "Doctoral",
            amirkabir,
            19,
        )
        ee.add_students(s1, s2, s3, s4)
        self.assertIn(s2, ee % 17)
        self.assertIn(s3, ee % 17)
        self.assertIn(s4, ee % 17)
        p1 = Professor(
            "Amir",
            "Jahanshahi",
            date(1980, 1, 1),
            "Male",
            None,
            "Assistant Professor",
            amirkabir,
            1000000,
        )

        p2 = Professor(
            "Reza",
            "Sarraf Shirazi",
            date(1960, 1, 1),
            "Male",
            ee,
            "Associate Professor",
            amirkabir,
            1100000,
        )
        p3 = Professor(
            "Iman",
            "Shraifi",
            date(1970, 1, 1),
            "Male",
            ee,
            "Assistant Professor",
            amirkabir,
            105000,
        )
        p4 = Professor(
            "Mehrdad",
            "Abedi",
            date(1950, 1, 1),
            "Male",
            ee,
            "Professor",
            amirkabir,
            1200000,
        )
        ee.add_professors(p2, p3, p4)
        self.assertTrue(s2 in ee)
        self.assertTrue(s3 in ee)
        self.assertFalse(p1 in ee)
        self.assertTrue(p2 in ee)
        self.assertTrue(p4 in ee)

    ## ---------------- Aphw5 Test - 1 Test ----------------
    def test_aphw5(self):
        amirkabir = University(
            name="Amirkabir University of Technology",
            established=1928,
            chancellor="Seyed Ahmad Motamedi",
        )
        ee = Faculty("Electrical Engineering", amirkabir)
        read_data(amirkabir, ee, "test_aphw5.txt")
        bh = ee.get_top_remain("Bachelor")
        t1 = next(bh)
        with Timer() as t:
            t2 = next(bh)
        print(t.total * 1000)
        self.assertEqual(True, t.total * 100 < 0.01)
        self.assertEqual(t1.first_name, "f1419")
        self.assertEqual(t1.gpa, 19.98)
        self.assertEqual(t2.last_name, "l2266")
        self.assertEqual(t2.gpa, 19.97)


if __name__ == "__main__":
    unittest.main()

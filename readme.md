


# Introduction
In this homework we will implement some classes and learn python more.

# Person Class
This class represents each person. arguments of constructor of this class are first_name, last_name, birthday and gender respectively!
- birthday is private variable.
- This class cannot be instantiated.

# Student Class
Arguments of constructor of this class are first_name, last_name, birthday, gender, faculty, academic_degree, university and gpa respectively.
- default value of gpa is 15.
- academic rank must be
	- Bachelor
	-  Master
	-  Doctoral

  otherwise raise ValueError.
- faculty and university are instances of class Faculty and University.
- each student has a unique student number that is 6-digits random number. Note that student number is immutable, So the following code must raise ConstError.

    ```python
    amirkabir = University(name="Amirkabir University of Technology", established=1928, chancellor="Seyed Ahmad Motamedi")
    ee = Faculty("Electrical Engineering", amirkabir)
    s1 = Student("Mohammad Mahdi", "Shojaefar", date(1999,8,29), "Male", ee, "Bachelor", amirkabir, 12)
    s1.std_num = 123456
    ```
- ConstError is not python built in exceptions and you should implement it in exceptions.py!
- get_age() is a method of this class and return yout age. if today is 2/2/2021 and birthday is 1/2/2000 you should return 21 and if birhday is 3/2/2000 you should return 20.
- This class should be printable and print an expression like this:
'''I am (first name) (last name) and studying at (university)'''

# Professor Class
Arguments of constructor of this class are first_name,  last_name,  birthday,  gender,  faculty,  academic_rank,  university and salary respectively.

- salary is private variable.
- This class should be printable and print an expression like this:
  '''I am (academic rank) (first name) (last name) and studying at (university)'''
- academic rank can be
	- Professor
	- Associate Professor
	- Assistant Professor
	- Lecturer
  otherwise raise ValueError.
- get_age() is a method of this class.

When Ali realize that salary of each Professor is private he decide to write a function to divulge their salary but he don't know how to do it. Help Ali and complete function below. This function get the object of professor and return his/her salary! Write this function in aphw5.py!

```python
def  hack_salary(professor_obj):
	pass
```

Classes Person, Student and Professor are in person.py :)

#  University Class
member variable of this class are name,  established,  chancellor and faculties.

We have 2 constructors.
- you get a filename that name, established and chancellor stored in it respectively.
- you get name, established and chancellor unordered.
- This class should be printable and print an expression like this:
'''Here is (name)'''
- method which_university_is_this get a student number and return the university that this student is in.
- method add_facultiies get some faculties and add them to faculties list.
- You can only create 3 instance of class university. If we try to create more, you should raise RuntimeError. 


# Faculty Class
Required argument of constructor of this class are name and university.
optional argument are students and professors that student is tuple and professors is list.
- add_students() and add_professors() are 2 methods that get some objects and add them to professor list or students tuple!
- get_top_remain() get a degree and return the student with top gpa in specified academic degree when code below runs:
	```python
	amirkabir = University(name="Amirkabir University of Technology", established=1928, chancellor="Seyed Ahmad Motamedi")
	ee = Faculty("Electrical Engineering", amirkabir)
	s1 = Student("Mohammad Mahdi", "Shojaefar", date(1999,8,29), "Male", ee, "Bachelor", amirkabir, 12)
	ee.add_students(s1)
	bh = ee.get_top_remain('Bachelor')
	print(next(bh))
	```
- if we add a professor to a faculty, you should add this professor to professors list.
- if we sum two faculties together, you should change the first faculty and add other faculty professors to the first one. 
- you should return a list consist of all students that have gpa>=n by operator %. for example ```ee%16```  get  a list of all students that their gpa is not less than 16. you must use python filter and write this operator in 2 lines.
- code below must work
	```python
	amirkabir = University(name="Amirkabir University of Technology", established=1928, chancellor="Seyed Ahmad Motamedi")
	ee  =  Faculty("Electrical Engineering",  amirkabir)
	s1  =  Student("Mohammad Mahdi",  "Shojaefar",  date(1999,8,29),  "Male",  ee,  "Bachelor",  amirkabir,  16)
	p1  =  Professor("Amir",  "Jahanshahi",  date(1980,1,1),  "Male",  ee,  "Assistant Professor",  amirkabir,  1000000)
	ee.add_students(s1)
	ee.add_professors(p1)
	print(p1 in ee)
	print(s1 in ee)
	```
	It return True if this professor/student is in this faculty.

Classes Faculty and University are in university.py :)

# Aphw5 file
If you are here, congratulations. we have 2 other problems:
- code below must run:
	```python
	with Timer() as t:
		#To Do
	 ```
	 If we run a code in this with block, you should print a expression that show how much this code last to run. for example output of code below is ```629.26865 milliseconds```  
	```python
	with Timer() as t:
		[x for x in range(10000000)]
	```
- For the last one, you should implement a function that get an university, faculty and a file name that each line of that, is personal information of a student and then add them in the faculty.

**Note: Run each test separately.**

**Questions:**

- What is the output of code below? What happen if we comment line 4. explain it.
	```python
	def check():
		try:
			print("Try")
			return True
		except:
			print("Except")
		else:
			print("Else")
		finally:
			print("Finally")
			return False

	print(check())
	```

- How we can hack python getters and setters?

<br>

# Static Variable - A static attribute (also called a class attribute) is a variable that belongs to the class itself, not to individual objects. This means all objects of the class share the same variable.

# Key Points:
# 1) Defining a Static Attribute : Static attributes are defined inside the class but outside any method.
# 2) Modify using class name (recommended)
# 3) Modifying using object name
class Student:
    schoolName = 'Warren Academy School' # Static Attribute of the class
    def __init__(self, rollNumber, section):    # constructor
        self.rollNumber = rollNumber
        self.section = section
    
# main

student1 = Student(21, 'A')
print(student1.schoolName)
print(Student.schoolName)
Student.schoolName = 'Turtles' # modified using class name
print(Student.schoolName)

student1.schoolName = 'Somani International School' # modified using object name
print(student1.schoolName)
print(Student.schoolName)

# common use of Static Attribute are basically for counting the objects
# class Student:
#     count = 0   # static attribute

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# s1 = Student("Kunal")
# s2 = Student("Rahul")
# s3 = Student("Amit")

# print("Total Students:", Student.count)

# What @Staticmethod can't do
# 1) can't access instance variables - because @Staticmethod does not use (self)
# class Student:

#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def show():
#         print(self.name)   # ERROR

# 2) Cannot Access Class Variables Automatically - Because (cls) is not available.

    # This example will Throw an error
    # class Student:
    #   school = "JECRC"

    #   @staticmethod
    #   def show_school():
    #       print(school)   # ERROR

    # This example is correct
    # class Student:
    #   school = "JECRC"
    #   @staticmethod
    #   def show_school():
    #       print(Student.school)

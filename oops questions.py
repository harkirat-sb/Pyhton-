# # Define a class Person with the following attributes:
# #
# # name
# # age
# # Include the following methods:
# #
# # _init_(): Initialize the attributes.
# # display_info(): Print the person's name and age.
# # Write a program to create an instance of Person, set its attributes, and call the display_info() method.
#
#
#
# class employee :
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def display_info(self):
#         print(f"Name: {self.first_name}")
#         print(f"Name:{self.last_name}")
#         print(f"Age: {self.age}")
#
#
#
# person_1 = employee("Harkirat","Bhatia",18)
# person_1.display_info()
#
#
#
# # Define a class Rectangle with the following attributes:
# #
# # width
# # height
# # Include the following methods:
# #
# # _init_(): Initialize the attributes.
# # area(): Return the area of the rectangle.
# # perimeter(): Return the perimeter of the rectangle.
# # Write a program to create an instance of Rectangle, calculate its area and perimeter, and print the results.
#
#
# class Rectangle :
#     def __init__(self,length ,breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def area_rectangle(self):
#         result = self.length * self.breadth
#         return result
#
#
# rectangle_1 = Rectangle(10,40)
# print(rectangle_1.area_rectangle())
#
#
#
#
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#     def area_rec(self):
#         result = self.length*self.breadth
#         return result
#
#     def peri_rec(self):
#         result = 2*(self.length + self.breadth)
#         return result
#
# rectangle_2 = Rectangle(20,35)
# print(rectangle_2.area_rec())
# print(rectangle_2.peri_rec())
#
#
#
# # Define a class Counter that tracks the number of instances created. Include:
# #
# # An _init_() method to initialize the instance count.
# # A class method get_instance_count() that returns the total number of Counter instances.
# # Write a program to create multiple instances of Counter and use the class method to display the total count.
#
#
#


class Student:
    def __init__(self,Name,Marks1,Marks2,Marks3):
        self.Name = Name
        self.Marks1 = Marks1
        self.Marks2 = Marks2
        self.Marks3 = Marks3

#     def average_marks(self):
#         result = (self.Marks1+self.Marks2+self.Marks3)/3
#         return result
#
# s1 = Student("Harkirat", 90,92,85)
# print(s1.Name)
# print(s1.average_marks())
#





# # Define a class Person with the following attributes:
# #
# # name
# # age

# # Include the following methods:
# #
# # _init_(): Initialize the attributes.
# # display_info(): Print the person's name and age.
# # Write a program to create an instance of Person, set its attributes, and call the display_info() method.


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

s1 = person("Harkirat",18)

s1.display_info()

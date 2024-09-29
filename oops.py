class Employee:
     def __init__(self ,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "" + last + "@company.com"
     def __repr__(self):
         return "Employee({0},{1},{2})".format(self.first,self.last,self.email)
     def __str__(self):
         return "Employee({0}-{1})".format(self.first,self.last)

emp_1 = Employee("Harkirat",'Bhatia',100000)
emp_2 = Employee('Pragun',"Aggarwal",600000)
print(emp_1.__str__())
print(emp_1.__repr__())
#
#
# # class = blue print for creating instances
#
# # instances =  each employee we create using  class is intsnace of class

emp_1 = Employee("Harkirat",'Bhatia',100000)
emp_2 = Employee('Pragun',"Aggarwal",600000)
#
# print(emp_1)
# print(emp_2)
#
#
# print("{} {}".format(emp_1.first,emp_1.last))
#  # emplaoyee class  variable - contains data that is unique to each employee
#
# # emp_1.first = "Harkirat"
# # emp_1.second = "Singh"
# # emp_1.email = "Harkirat.3724@gmail.com"
# emp_1.pay  = 50000
# #
# # emp_2.first  = "Test"
# # emp_2.last  = "User"
# # emp_2.email  = "Test user@gmail.com"
# emp_2.pay  = "60000"
# # print(emp_2.email)
# #  print(emp_1.email)
# # # to automatially create these information we domt have tp write a lpng code we  can idrecly use the init method
#
#
# emp_1.pay  = 100000
# Employee.raise_amount = 1.05
#
class Employee:
      raise_amount = 1.04

      def __init__(self,first,last,pay):
         self.first = first
         self.last = last
         self.pay = pay
         self.email = first + "" + last + "@company.com"


#
#
#      def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#      def fullname(self):
#         return "{} {}".format(self.first,self.second)
#
#      @classmethod
#      def set_raise_amount(cls,amount):
#       cls.raise_amount = amount
# Employee.set_raise_amount(1.05)
#
# print(emp_1.pay)
# # emp_1.raise_amount = 1.05
# # #print(emp_1.pay)
# #
# # print(emp_2.pay)
# # #
# # print(emp_2.pay)
# #
# #
# # #This is a class method
# #
# #
# #
# # emp_1 = Employee("Harkirat",'Bhatia',100000)
# # emp_2 = Employee('Pragun',"Aggarwal",600000)
# #
# # Employee.set_raise_amount(1.05)
# #
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)
# # #abhi ise sabka same hoga that is 1.04
# # #agar mein class method use karenge to use we can raise amount
# #
# #
# # print('Hello')
# #
# # emp_str_1 = "Harkirat-bhatia-2000"
# # first,last,pay = emp_str_1.split("-")
# # new_emp_1 = Employee(first,last,pay)
# # print(new_emp_1.email)
#
# @classmethod
# def from_string(cls,emp_str):
#     first,last,pay = emp_str.split("-")
#     Employee(first,last,pay)
#     return cls(first,last,pay)
# # emp_str_2 - "jasroop,sachedva,10000"
# # new_emp_2 = Employee.from_string(emp_str_2)
# # print(new_emp_2.pay)
#
#
#
# #static methods
# #
# # @staticmethod
# # def is_workday(day):
# #     if day.weekday() == 5 or  day.weekday() == 6:
# #         return False
# #     return True
# # import datetime
# # my_date = datetime.date(2022,9,24)
# # print(Employee.is_workday(my_date))
# #
#
# #inheritecnce
#
#
# class Developer(Employee):
#     def __init__(self,first,last,pay,prog_lang):
#         super().__init__(first, last, pay)#how to call the parent class
#         self.pro_lang = prog_lang
# dev_1 = Employee("harkirat","Bhatia",10000,"python")
# print(dev_1.email)
# print(help(Developer))
# print(dev_1.pay)
# dev_1.raise_amount()
# print(dev_1.pay)

def __repr__(self):
    return "Employee({0})".format(self.first)

class Employee:
    def __init__(self ,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "" + last + "@company.com"
    def fullname(self):
        return "{} {}".format(self.first,self.last)

emp_1 = Employee("John","Smith",30000)
#if first name is changed it will be shown in full name but not in email
emp_1.first = "Jim"
print(emp_1.email)
print(emp_1.fullname())

#method 1

class Employee:
    def __init__(self ,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "" + last + "@company.com"
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    @property
    def email(self):
        return "{}.{} @gmail.com".format(self.first,self.last)
#full name settter
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(" ")
    self.first = first
    self.last = last
    @fullname.deleter
    def fullname(self):
        print('KUCH HAI NAHI ')
        self.first = "None"
        self.last = "None"
emp_1 = Employee("John","Smith",30000)
emp_1.fullname = "Harkirat Singh"
print(emp_1.email)
print(emp_1.fullname  )

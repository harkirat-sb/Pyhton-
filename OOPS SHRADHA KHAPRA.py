# #Sstatic method
#
# # in static methods we dont have to define self paremeter ,
# #  they work at class level
# #    for a static method we use @static method  called as a decorator
#
# # 4 pillars of oops
# # Abstraction - hiding implementation details of class ,,, class mein implimentation hide karliya sirf important detias dikhayi...
#
# class CAR:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started")
#
# car1 = CAR()
# car1.start()
#
# # Encapulation - cappsule of data and function in a single unit , jaise class mein objects ka attricbutes and methods define  KARE
#
#
# class Account:
#     def __init__(self,balance ,accountnumber):
#      self.balance = balance
#      self.accountnumber = accountnumber
#
#     def Debit(self,amount):
#      self.balance =- amount
#      print("RS,{} was debited".format(amount))
#
#     def Credit(self,amount):
#      self.balance =+ amount
#      print("RS,{} was credited".format(amount))
#
#     def get_balance(self,amount):
#      resultself.balance
#
#
#
# acc1 = Account(20000,3724)
# print(acc1.balance)
# print(acc1.accountnumber)
# #
# # print(acc1.get_balance)
# #
# # acc1.Debit(10000)
# #
# #
# # #PART2 OOPS
# #
# # # del keyword-used to delete object properties or object itsekf
# #
# #
# #
# class Students:
#     def __init__(self,name):
#         self.name = name
#
# s1 = Students('Harkirat ')
# del s1
# print(s1.name)
# del s1.name
# print(s1.name)

#
# # in oops we have concept of public and private  in python aagr koi method ya attribute ko ham class ke bhar bhi use  kar sakte hai but on baaki lamguages ham bhar use  nahi kar sakte hai .....
# # for example jo name ham print  karte hai wo class se bahar karte hai in python `  `
#
# # class account:
# #     def __init__(self,acc_no,acc_pass):
# #         self.acc_no = acc_no
# #         self.__acc_pass = acc_pass
# #     def reset_pass(self):
# #
# #         acc1 = account(99880,3724)
# # # ab yeh iinformation ko private karna hai as it is avialable in public domain so we  will use double under score jise information will becpme private
# # print(acc1.acc_no)
# # print(acc1.__acc_pass)
# #
# # # print(self.__acc_pass)
# # # yeh chaljayge becayse yeh class ke andar hai hence it will  work it will be public,,,
#
#
#
# class person:
#     __name = "Anonymus"
#
#     def __hello(self):
#         print("Hello Person !")
#
#     def welcome(self):
#         self.__hello()
# p1 = person()
# print(p1.__hello())
# # private attributes  methods which are meant to be used within the class and not accesible from outside
#
# # inherit when one class derives the properties and  methods of another class +4+88+


# class Car:
#     @staticmethod
#     def start():
#         print("Car Started")
#
#     @staticmethod
#     def stop():
#         print('Car stopped...')
#
#
#     class ToyotaCar(Car):
#         def __init__(self,name):
#             self.name  = name
#
# Car1 = ToyotaCar("Fortuner")
# Car2 = ToyotaCar("Virtus")
#
# print(car1.start())
###even though we have not defined for  clSS TOYOTA CAR but we have used inheeritence hence jo hamne phele ke life define kiya can be used for next inheritence is used by usinf parathesis and adding clss name in it (car)

#Single inheritience - jiski ek parent class ho  aur ek child class ho


# multileve inheritence - jab ek base class se hamne dusri class derivekare and fir use derive class se ham ek aur derived class derive kare is multilevel
# there can be more than 2 derived levels

class Car:
    @staticmethod
    def start():
        print("car Started")

    @staticmethod
    def stop():
        print('car stopped...')

class ToyotaCar(Car):
    def __init__(self,brand):
        self.name  = name


class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

Car1 = Fortuner("Deisel")
Car1.start()

# MULTIPLE INHERITENCE
# DO ALAG ALG PARENT CLASS SE DERIVE KARKAE EK DERIVED CLASS LI HAI(#2 se zyada bhi ho sakte hai base class )


class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"
c1 = C()
print(c1.varA)
print(c1.varC)
print(c1.varB)

# Super method- access methods of parents  class(#calling of parent class in derived class)

# class Car:
#
#     def __init__(self,type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car Started")
#
#     @staticmethod
#     def stop():
#         print('car stopped...')
#
# class ToyotaCar(Car):
#      def __init__(self,name,type):
#         self.name  = name
#         super().__init__(type)
#         super().start()
# car1 = ToyotaCar("PRIYUS","ELECTERIC")
# print(car1.type)
#
# #CLASS METHOD KA IMPACT
#
# class Person:
#     name = "Anonymous"
#     def changename(self,name):
#         Person.name = name
#
# p1 = Person()
# p1.changename("Rahul kumar ")
# print(p1.name)
# print(Person.name)
# #DIRECTLY AGAR FUNCTION LE ANDAR CLASSKO DEFINE LARDE
# class Person:
#     name = "Anonymous"
#     def changename(self,name):
#         self.__class__.name = "Rahul "
#
# p1 = Person()
# p1.changename("Rahul")
# print(p1.name)
# print(Person.name)
#
# # class method wha use karte hai jha par static method  nahi chalte
# #class method isme argumet class hota hai and we use at the rarte class method
#
# class Person:
#     name = "Anonymous"
#     @classmethod
#     def changename(cls,name):
#         cl s.name = name
#
# p1 = Person()
# p1.changename("Rahul kumar ")
# print(p1.name)
# print(Person.name)


class Students:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
st1 = Students(99,98,100)
print(st1.percentage)

#agar ek ke marks change hote hai to we  have tp define a new methpd usinf def calpercentage
# we use @property

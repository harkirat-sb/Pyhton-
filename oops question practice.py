# class Car:
#     def __init__(self,model,year,type):
#         self.model = model
#         self.year = year
#         self.type = type
#     def display_info(self):
#         return"hey !This car is {0},{1} launched in {2}".format(self.type,self.model,self.year)
#
# car_1 = Car("DF3",2014,"Petrol")
# car_2 = Car("GGF3",2024,"Ev")
#
# print(car_1.display_info())
# print(car_2.display_info())



class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def hello(self):
        print("Hello!I am {}.".format(self.name))

class Dog(Animal):
    def __init__(self,name,type,breed):
        self.breed = breed
        super().__init__(name,type)
    def speek(self):
        result = "Hey!,I am  {} and a {}".format(self.name,self.type)
        return result


Dog_1 = Dog("Tyson","dog","lebra")
print(Dog_1.speek())
Dog_1.hello()




class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class ElectricCar(Car):  # Correct the spelling of ElectricCar
    def __init__(self, brand, model, battery_percentage):  # Rename parameter for clarity
        super().__init__(brand, model)
        self.battery_percentage = battery_percentage  # Fix typo

car1 = ElectricCar("Tata", "Nexon", 90)
print(f"Brand: {car1.brand}, Model: {car1.model}, Battery Percentage: {car1.battery_percentage}%")








class Animal:
    def __init__(self,speices):
        self.speices = speices
    def make_sound(self):
        return "Some sound"
class Dog(Animal):
    def __init__(self,speices):
        super().__init__(speices)
    def make_sound(self):
        return "Woof,Woof of a Dog!"
Dog_1 = Dog("Lebra")
print(Dog_1.make_sound())
Animal_1= Animal("Lebra")
print(Animal_1.make_sound())

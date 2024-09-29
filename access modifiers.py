class Employee:
    def __init__(self):
        self.__name= "Harry"

a = Employee()
#print(a.name)
#by default accesible from outside
#it is a type of idcator of being private but still can be used by ,,,
print(a._Employee__name) # can be accessed indirectly
print(a.__dir__())

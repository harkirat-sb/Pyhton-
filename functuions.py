# #
# # def multiply(x,y):
# #     result = x * y
# #     return result
# #
# #
# #
# # answer = multiply(10.5,4)
# # print(answer)
# #
# #
# # answer = multiply(6,7)
# # print(answer)
# #
# # forty_two = multiply(6,7)
# # print(forty_two)
# #
# # #palindrome solution
# # #
# # def is_palindrome(string):
# #      # backwards = string[::-1]
# #      # return backwards == string
# #      return string[::-1].casefold == string.casefold
# #
# #
# # def palindrome_sentence(sentence):
# #     string=""
# #     for char in sentence:
# #         if char.isalnum():
# #             string += char
# #     print(string)
# #     return string[::-1].casefold == string.casefold
# #
# #
# # word = input("Please enter a word to check:")
# # if palindrome_sentence(word):
# #      print("'{}' is  a palindrome".format(word))
# # else:
# #      print("'{}' is not a palindrome".format(word))
#
# #
# # def hello_func(greeting,name = "You"):
# #      return "{},{} Function.".format(greeting,name)
# #
# # print(hello_func("Hi", name = "Corey"))
#
#
# # DRY- DONT REPEAT YOURSELF USE DEF FUNCTIONS
# courses ={}
#
# def student_info(*args,**kwargs):
#      print(args)
#      print(kwargs)
#
# student_info("Math",'ART',name = "JOHN",age=22)
#
# courses = {'Math',"ART"}
# info = {"name":"John","age":22}
# student_info(*courses,**info)



#
#
#
# def calc_sum(a,b):
#      sum = a + b
#      print(sum)
#      return sum
#
# calc_sum(5,10)
#
# calc_sum(17,12)
#
#
#
# def print_hello():
#      print("Hello")


def aver_numbers(a,b,c):
     average = (a + b + c )/3
     print(average)
     return average


aver_numbers(4,7,7)
 

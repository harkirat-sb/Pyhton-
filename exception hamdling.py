#
# a = int(input("Please enter your Number: "))
# print("Multiplication table of {}".format(a))
# for i in range(1, 11):
#     result = a * i
#     print("{} X {} is {}".format(a, i, result))
#
#
# # print("Some imp lines of code")
# # print("End of Programme")
#
# # isko ab ham modify karneg aise ki in case of same error wo hame apolgy message dikhadenge and baaki ka code run lkardega except the error part bit it wont show any error
#
#
#
#
# a = (input("Please enter your Number: "))
# print("Multiplication table of {}".format(a))
# try:
#     for i in range(1, 11):
#      result = int(a * i)
#      print("{} X {} is {}".format(a, i, result))
# except:
#       print("Invalid Input!")
#
# print("Some imp lines of code")
# print("End of Programme")

# try:
#     num = int(input("Enter an integer:"))
#     a = [3,6]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer")
#
# except IndexError:
#     print("Index Error")

#Value error is used when a string is being tried to convert to integer
#inde error is used when a number outisde the range is used

#
#
# try:
#     f = open("textfilee.txt")
#     var = bad_var
# except FileNotFoundError:
#     print("Error! File doesnot exist hehee>>> bitchhhh")
# except Exception:
#     print("Sorry s omething went wrong .......")



try:
    f = open("practice.txt.py")
except FileNotFoundError:
    print("File not present")
except Exception:
    print("Error")
else:
    print(f.read())
    f.close()
finally:
    print("Excecuting finally")

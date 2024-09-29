name= input("Please enter your name; ")
age= int(input("How old are you,{0}?".format(name)))
print(age)

#if age >= 18:
# print('You are old enough to vote')
#    print("please put x in the box")
# else:
#    print("Please comeback in {0} years" .format(18-age))
if age < 18:
     print("Please comeback in {0} years".format(18-age))
elif age == 100:
    print('Sorry, Today you die in return of jedi ')
else:
     print('You are old enough to vote for the country')
     print("Please educate people about this ")

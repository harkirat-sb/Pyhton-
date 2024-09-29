

name = input('Enter your Name here:')
age=  int(input('How old are you ? '))
if age >= 18 and age < 31:
    print("Hello {0},Welcome to the club 18-30 Holidays".format(name))
else:
    print("Sorry{0},You are not allowed".format(name))

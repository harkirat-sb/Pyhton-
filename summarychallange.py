choice = "-"

while choice != "0":
    if choice in "12345":
        print('You chose {}'.format(choice))

    else:
        print("Please select from the option below")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("0:\texit")

    choice = input()

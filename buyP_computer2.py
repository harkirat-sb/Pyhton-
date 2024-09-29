current_choice = "-"
computer_parts = []


while current_choice != "0":
    if current_choice in "12345":
        print("{} is added".format(current_choice))
        if current_choice == "2":
            computer_parts.append("graphic card")
        if current_choice == "1":
            computer_parts.append("computer")
        if current_choice == "4":
            computer_parts.append("track pad")
        if current_choice == "5":
            computer_parts.append("thermal pad")
            if current_choice == "6":
                computer_parts.append("hdmi cabel")

        else:

            print("Please add other option")
            print("1: please add computer")
            print("2: please add  oled or led")
            print("3: please add graphic card")
            print("4: please add track pad")
            print("5: please check thermal pad")
            print("6: hdmi cabel")
            print("0: to finish")


current_choice = input()

print("computer_parts")

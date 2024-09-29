current_choice = "-"
computer_parts = []
available_parts =["computer",
                  "oled or led",
                  "graphic card",
                  "trackpad",
                  "thermal pad"
                  ]
valid_chouces=[]
for i in range(1,len(available_parts)+1):
    valid_chouces.append(str(I))

while current_choice != "0":
    if current_choice in "12345":
        print("{} is added".format(current_choice))
        if current_choice == "3":
            computer_parts.append("graphic card")
        if current_choice == "1":
            computer_parts.append("computer")
        if current_choice == "4":
            computer_parts.append("track pad")
        if current_choice == "5":
            computer_parts.append("thermal pad")
        if current_choice == "2":
            computer_parts.append("oled pr led")
        else:

            print("Please add other option")
            print("1: please add computer")
            print("2: please add  oled or led")
            print("3: please add graphic card")
            print("4: please add track pad")
            print("5: please check thermal pad")
            print("0: to finish")


current_choice = input()

print(computer_parts)


current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in "12345":
        print("{} is added".format(current_choice))
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("oled or led")
        elif current_choice == "3":
            computer_parts.append("graphic card")
        elif current_choice == "4":
            computer_parts.append("track pad")
        elif current_choice == "5":
            computer_parts.append("thermal pad")
    else:
        print("Please select an option:")
        print("1: Add computer")
        print("2: Add oled or led")
        print("3: Add graphic card")
        print("4: Add track pad")
        print("5: Add thermal pad")
        print("0: Finish")

    current_choice = input("Enter your choice (0-5): ").strip()

print("Selected computer parts:", computer_parts)

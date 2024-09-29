shopping_list = ["milk", "pasta","eggs", "rice"]







#for item in shopping_list:
#    if item != 'rice':
#        print('BUY '+ item)



for item in shopping_list:
    if item == "spam" :
        continue


    print("Buy" + item)

for item in shopping_list:
    if item == "eggs" :
         break


    print("Buy" + item)

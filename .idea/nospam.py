menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "   sausage", "spam"],
    ["spam", "bacon", "sausag e", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

#no spam challange

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end="  ")


    print()

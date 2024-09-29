shopping_list = ["milk","pasta","eggs","bread","rice"]

item_to_find = "eggs"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:
    print('Item found at position {}'.format(found_at))
else:
    print("{} not found ".format(found_at))

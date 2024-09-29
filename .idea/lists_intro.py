
computer_parts = ['computer',
                  'monitor',
                  'keyboard',
                  'graphic card',
                  'mouse',
                  'mat']


for part in computer_parts:
    print(part)



print(computer_parts[2])



print(computer_parts[0:3])

print(computer_parts[-1])

result = True
another_result = result
print(id(result))
print(id(another_result))



result2 = False

print(id(result2))

computer_parts[3] = "trackball"
print(computer_parts)
computer_parts

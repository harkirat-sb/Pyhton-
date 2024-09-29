pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)

print(letters)

numbers = [2.3,4.5,8.7,3.1,9.3,2,1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)



numbers.sort()
print(numbers)



missing_letter = sorted("The quick brown fox jumps over the lazy dog ",
                        key=str.casefold)
print(missing_letter)



names = ['Graham',
         'Colin',
         'Pearson',
         'specter',
         'litt'
         ]
names.sort()
print(names)

names.sort(key=str.casefold)
print(names)

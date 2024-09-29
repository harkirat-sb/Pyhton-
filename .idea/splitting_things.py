pangram = 'The quick brown fox jumps over the lazy dog '

words = pangram.split()
print(words)


pangram = """The quick brown
fox jumps\tover
the lazy dog"""
words = pangram.split()
print(words)



numbers = "9,223,372,036,854,775,807"
print(numbers.split(','))


# values = "". join(char if char not in separators else ' ' for char in numbers).split()



generated_list = ['9',' ',
                  '2','2','3',' ',
                  '3','7','2','',' ',
                  '0','3','6',' ',
                  '8','5','4',' ',
                  '7','7','5',' ',
                  '3','7','2','1',' ',]




values = "".join(generated_list)
print(values)


values_list = values.split()
print(values_list)

answer=6
print('Please guess the number between 1 and 10')
guess=int(input())

if guess == answer:
    print("You won in the first trial")
else:
    if guess < answer:
        print( 'GUESS MUST BE HIGHER')
    else:
        print("GUESS MUST BE  LOWER")
    guess = int(input())
    if guess == answer:
        print('WELL done you guessed it ')
    else:
        print('SORRY NOT GUESSED')

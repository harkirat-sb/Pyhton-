answer=5

print(" Please guess the number between 1 and 10:")
guess=int(input())

#if guess<answer:
#    print('Please guess higher')
#   guess= int(input())
#if guess ==answer:
#   print('Well done you guessed it' )
#elif guess>answer:
#    print("Please  guess lower")
#    guess= int(input())12
#if guess ==answer:
#   print('Well done you guessed it')
#else:
#   print('You won meri baby girl')


answer=5

if guess != answer:
    if guess < answer:
        print('Please guess again')
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print('Well Done')
    else:
        print("sorry you are not correct1")
else:
    print('You got it first time')

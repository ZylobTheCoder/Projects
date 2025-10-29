import random
a = random.randint(1,101)
b = int(input('Guess the number(Hint,its from 1 to 100)'))
while True:
 if a > b:
    print('Guess higher')
    b = int(input('Guess the number(Hint,its from 1 to 100)'))
 elif a == b:
    print('Exactly correct')
    break
 elif a < b:
    print('Guess lower')
    b = int(input('Guess the number(Hint,its from 1 to 100)'))
score = 0
q1 = input('What is also known as the red planet?\na)Mars b)Saturn c)Venus d)None of the above (a/b/c/d): ')
if q1 == 'a':
    print('Correct!')
    score += 1
else:
    print('Wrong')    
q2 = input('In which year did India got indepence?\na)1953 b)1947 c)1951 d)1971(a/b/c/d): ')
if q2 == 'b':
    print('Correct!')
    score += 1
else:
    print('Wrong')    
q3 = input('What is full form of WHO?\na)World heredity organization b)War Hazard organization c)World Health Organization d)None of the above(a/b/c/d): ')
if q3 == 'c':
    print('Correct!')
    score += 1
else:
    print('Wrong')    
q4 = input('How many nights are in a fortnight?\na)Four b)Fourty c)Fourteen d)none of the above (a/b/c/d): ')
if q4 == 'c':
    print('Correct!')
    score += 1
else:
    print('Wrong')    
q5 = input('Which country is the most populated as of 2025? \na)India b)USA c)China d)Russia (a/b/c/d): ')
if q5 == 'a':
    print('Correct!')
    score += 1
else:
    print('Wrong')
while True:    
 Q = int(input('Guess how many you scored correct (0/1/2/3/4/5): '))
 if Q == score:
    print('Yup')
    break
 else:
     print('Try again')
     Q = int(input('Guess how many you scored correct (0/1/2/3/4/5): '))
       
print('Out of 5 questions,you scored',score,'correct.')
while True:
 Q1 = int(input('How much would you rate this program out of 5? Your feedback helps us a lot!'))
 if Q1 >= 0:
    if Q1 <= 5:
      print('Thanks for your feedback!')
      break
 elif Q1 < 6:
    print('Try again')
    break  

    




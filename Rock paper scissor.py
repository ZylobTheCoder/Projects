R = 'Rock'
P = 'Paper'
S = 'Scissor'
Q = input('Welcome to Rock Paper Scissor game,Choose Rock or Paper or Scissor (R/P/S)')
while True:
 if Q == 'R':
    print(P)
     
 elif Q == 'P':
    print(S)
     
 elif Q == 'S':
    print(R)
    
 else:
    print('Error,try again')
    Q = input('Choose Rock or Paper or Scissor (R/P/S)')

 print('You lost, haha!')
 print('Thanks for playing the game!')
 Q2 = input('Wanna try again? (y/n)')
 if Q2 != 'y':
   print('See you,Scaredy cat🤣')
   break
 else:
    Q = input('Welcome to Rock Paper Scissor game,Choose Rock or Paper or Scissor (R/P/S)')
    

  

P = float(input('enter the principal: '))
T = float(input('enter the time in years: '))
R = float(input('enter the rate of interest(in percent): '))
C = input('Enter your currency (eg-INR,Dollars,Euros): ')
SI = (P*T*R)/100
print('Your simple interest is',SI,C)
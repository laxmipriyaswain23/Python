#Wap input 2 number perform calculations based on user input
from audioop import add
from secrets import choice


a=int(input('Enter the value for a'))
b=int(input('Enter the value for b'))
ch=input('Enter a choice \n add \n sub \n mul \n div \n')

if ch=='add':
    print(a+b)
elif ch=='sub':
    print(a-b)
elif ch=='mul':
    print(a*b)
elif ch=='div':
    print(a/b)
else:
    print('Invalid option')
            
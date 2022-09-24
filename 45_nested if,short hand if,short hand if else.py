#nested if
a=int(input('Enter a number'))
if a>=0:
    if a==0:
        print('Zero')
    if a>0:
        print('positive number')
if a<0:
    print('Negative number')        

#Short hand if
a=int(input('enter a value'))
b=int(input('Enter b value'))
if (a>b):   print(a,'is greater than',b)

#Short hand if else
i=int(input('Enter a value'))
print(True) if i>16 else print(False)
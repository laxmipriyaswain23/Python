#Wap to find out the value of y using
#y(x,n)={1+x when n=1,1+(x/n) when n=2,1+x^n when n=3,1+(n*x) when n>3 or n<1}

import math
x=int(input('Enter the value of x'))
n=int(input('Enter the value of n'))

if n==1:
    y=1+x
    print('The value of y is ',y)
elif n==2:
    y=1+(x/n)
    print('The value of y is ',y)
elif n==3:
    y=1+math.pow(x,n)
    print('The value of y is ',y)
else:
    y=1+(n*x)
    print('The value of y is ',y)
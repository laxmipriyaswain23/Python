#Wap to calculate the sum of numbers  from m yo n
m=int(input('Enter the value of m'))
n=int(input('Enter the value of n'))
result=0
while m<=n:
    result=result+m
    m=m+1

print(result)
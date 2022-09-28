#Wap to print a list in reverse order by using positive index
l=[10,20,30,40,50,60,70]
n=len(l)-1
while n>=0:
    print(l[n])
    n=n-1


#print list in reverse order by using negative index
l=[10,20,30,40,50,60,70]
i=-1
while i>=-len(l):
    print(l[i])
    i=i-1

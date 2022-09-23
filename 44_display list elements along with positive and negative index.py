#Wap to display list elements along with positive and negative index
l=[10,20,30,40,50,60]
n=len(l)
for i in range(n):
    print("{} is present at index {} /{}".format(l[i],i,i-n))

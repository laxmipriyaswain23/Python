#Using for loop traversing a list
l=[10,20,30,40,50]
for i in l:
    print(i)

#Traversing list using while loop
l=[11,22,33,44,55,66]
i=0
while i<=5:
    print(l[i])
    i=i+1

#when there is more number of data in a list
l=[99,88,77,66]
i=0
while i<=len(l)-1:
    print(l[i])
    i=i+1    


#when the data is divisible by 8 or 4 then print or add some condition
l=[99,88,77,66,45,29,28,24,14,56,34,35]
for i in l:
    if i % 4 == 0 and i % 8 == 0:
        print(i)    
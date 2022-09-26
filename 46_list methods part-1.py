#Ex-1
#append()
l=[10,20,30,40,50,60]
print(l)
l.append(999)
print(l)
l.append(78)
print(l)

#Ex-2
#Wap to create a list by adding 20 0's
l=[]
for i in range(20):
    l.append(0)
    
print(l)

#Ex-3
#Wap to create a list by adding 0 to 20
l=[]
for i in range(21):
    l.append(i)
    
print(l)

#Ex-4
#insert()
l=[11,22,33,44,55,66]
print(l)
l.insert(4,9999)
print(l)
l.insert(2,8675)
print(l)

#Ex-5
#if the specified positive index crossed the maximun index,then it will be inserted at the end of the list
l=[225,5,58,77,66,99,11]
print(l)
l.insert(20,5768)
print(l) 

print(l.index(5768))

#Ex-6
# if the specified negative index crossed the maximun index,then it will be inserted at the beginning of the list
l=[225,5,58,77,66,99,11]
print(l)
l.insert(-20,5768)
print(l) 

print(l.index(5768))

#Ex-7
#count()
l=[10,20,30,40,50,10,20,30,40,50]
print(l)
print(l.count(10))
print(l.count(20))
print(l.count(30))
print(l.count(40))
print(l.count(50))

#Ex-8
#index()
l=[20,30,48,57,69,20,30]
print(l)
print(l.index(20))
print(l.index(30))
#print(l.index(567)) #index out of range error

#Ex-9
#remove()
l=[10,20,30,40,10,20]
print(l)
l.remove(10)
print(l)
l.remove(20)
print(l)
#l.remove(456) #value error
#print(l)

#Ex-10
#Pop()
l=[10,20,30,40,10]
print(l)
print(l.pop())
print(l)
print(l.pop(2))
print(l)
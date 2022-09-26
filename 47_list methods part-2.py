#Ex-1
#extends()
l=[10,20,30,40,50,60]
print(l)
a=[11,22,33,44,55,66,77]
print(a)
l.extend(a)
print(l)

#Ex-2
oldGflist=['C','Java','Python','PhP','MySql']
print(oldGflist)
newGflist=['AI','ML','IoT','Blockchain','AR/VR']
print(newGflist)
oldGflist.extend(newGflist)
print(oldGflist)

#Ex-3
#reverse()
l=[44,55,66,77]
print(l)
l.reverse()
print(l)

#Ex-4
#sort()
l=[10,3,5,7,8,34,20,78,1,2,55,9,50]
l.sort()
print(l)

#Ex-5
#In desecnding order
l=[10,3,5,7,8,34,20,78,1,2,55,9,50]
l.sort(reverse=True)
print(l)

#Ex-6
#if the list contain number thn it will work based on ascending order,but if it contain string then it will work in alphabet order
l=['surendra','priyanka','rahul','zini']
l.sort()
print(l)

#Ex-7
# l=['surendra','priyanka','rahul','zini',1,2,3,44,55]
# l.sort()
# print(l) #type error/in python version 2 it will work and we will get the result like [1, 2, 3, 44, 55, 'priyanka', 'rahul', 'surendra', 'zini']


#Ex-8
#clear()
l=[11,22,33,44,55,66]
print(l)
l.clear()
print(l) # empty list 

#Ex-9
#copy()
l=[23,33,43,65,78]
s=l.copy() #cloning
print(l)
print(s)

print(id(l)) #2329690984256 different memory location
print(id(s)) #2329695277248

s[2]=456 #modify
print(l)
print(s) #after modify it will not affect to original list

#Ex-10
#assign
l=[23,33,43,65,78]
s=l
print(l)
print(s)

print(id(l)) #2693465625728
print(id(s)) #2693465625728 same memory location

s[2]=456 #modify
print(l)
print(s) #if modify in l list it will reflect to s list
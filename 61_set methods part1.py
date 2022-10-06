#Set Methods

#add()
#Ex-1
s={10,20,30,40}
s.add(23)
print(s)

#Ex-2
s={11,22,33,44}
s.add('laxmi')
print(s)

#Ex-3
s={10,20,30,40,50}
s.add(20)
print(s)

#update()
#Ex-4
s={10,20,30,40,50}
l=[1,2,3,4]
t=(11,22,33,44,55)
s.update(l,t)
print(s)

#Ex-5
s={22,33,44,55}
l=['surendra','priyanka','zini','kajal']
t=(1,2,3,4,5)
s.update(l,t,range(90,101))
print(s)

#Ex-6
s={11,22,33,44}
s.add(999)
print(s)

# #Ex-7
# s={11,22,33,44}
# s.add(999,78) #takes only single argument
# print(s) #Error

#Ex-8
s={11,22,33,44}
s.update([999,345]) #it takes iterable object as argument not integer
print(s) 

#Ex-9
s={11,22,33,44}
s.update(range(20),range(100,111))
print(s)

#remove()
#Ex-10
s={11,22,33,44}
s.remove(22)
print(s)

# #Ex-11
# s={11,22,33,44}
# s.remove(55)
# print(s) #key Error 55


#discard()
#Ex-12
s={11,22,33,44}
s.discard(22)
print(s)

#Ex-13
s={11,22,33,44}
s.discard(55)
print(s) #No error only get set as an output {33, 11, 44, 22}


#pop()
#Ex-14
s={11,22,33,44}
s.pop() #delete random element
print(s)

#Ex-15
s={11,22,33,44}
s.pop() #delete random element
print(s) #{11, 44, 22}
print(s.pop()) #11

# #Ex-16
# s={}
# s.pop() #here it is taken as an dict.
# print(s) #TypeError: pop expected at least 1 argument, got 0

# #Ex-17
# s=set()
# print(s.pop()) #KeyError: 'pop from an empty set'


#copy()
#Ex-18
s1={10,20,30,40}
s2=s1.copy()
print(s2)
print(s1) #same value
print(id(s1))
print(id(s2)) #pointing to different memory location

s1.add(1111) #the value is add to s1 not to s2 and it will not affect to s2 (swallow copy)
print(s1) 
print(s2) 


#Ex-19
s1={10,20,30,40}
s2=s1 #this means assign not copy
print(s2)
print(s1) #same value
print(id(s1))
print(id(s2)) #pointing to same memory location

s1.add(1111) #the value is add to s1 as well as s2 and it will  affect to s2(deep copy)
print(s1) 
print(s2) 


#clear()
#Ex-20
s={10,20,30,40,50}
print(s)
s.clear()
print(s) #set()

#enumerate()
#Ex-21
s={111,222,333,444,555,666}
for i in enumerate(s):
    print(i)


#max() and min()
#Ex-22
s={111,222,333,444,555,666}
print(min(s)) #111
print(max(s)) #666

#sum()
#Ex-23
s={111,222,333,444,555,666}
print(sum(s))  #2331

#sorted()
#Ex-24
s={10,220,30,4,50}
print(sorted(s))
print(sorted(s,reverse=True))


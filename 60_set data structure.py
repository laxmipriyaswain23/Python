#creation of set in different ways

#creation of empty set
#Ex-1
s={}
print(s)
print(type(s)) #create a dict. not a set

#another way for creating a empty set using set()
s=set()
print(s) #set()
print(type(s)) #<class 'set'>

#creation of set with multiple elements
#Ex-2
s={10,20,30,40,50}
print(s)    #{50, 20, 40, 10, 30}
print(type(s)) #<class 'set'>


#creation of set with heterogeneous elements
#Ex-3
s={10,20,30,40,50,'laxmi','surendra'}
print(s)    #{50, 20, 'laxmi', 40, 10, 'surendra', 30}
print(type(s)) #<class 'set'>


#creation of set using set()

#creation of set from list
#Ex-4
l=[11,22,33,44,55]
s=set(l)
print(s) #{33, 11, 44, 22, 55}
print(type(s)) #<class 'set'>

#creation of set from tuple
#Ex-5
t=(111,222,333,444,555)
s=set(t)
print(s) #{555, 333, 111, 444, 222}
print(type(s)) #<class 'set'>

#creation of set from range()
#Ex-6
s=set(range(10))
print(s) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(s)) #<class 'set'>

#creation of set from string
#Ex-7
name="Laxmi priya swain"
s=set(name)
print(s) #{'x', 's', 'r', 'm', 'n', 'p', 'L', ' ', 'y', 'w', 'a', 'i'}
print(type(s)) #<class 'set'>

#Ex-8
name="Laxmi priya swain"
s=set(name.split())
print(s)  #{'Laxmi', 'priya', 'swain'}
print(type(s)) #<class 'set'>

#Ex-9
s=set('laxmipriya')
print(s) #{'x', 'l', 'y', 'a', 'm', 'i', 'p', 'r'}
print(type(s)) #<class 'set'>

# #Ex-10
# s={10,20,30,40}
# print(s[2]) #TypeError: 'set' object is not subscriptable 

# #Ex-11
# s={10,2,30,40}
# print(s[::]) #TypeError: 'set' object is not subscriptable 

#Ex-12
#Applying membership operator in set (in and not in operator)
s={11,22,'surendra','rahul',78.98}
print('surendra' in s) #True
print('priyanka' in s) #False
print('priyanka'  not in s) #True
print('surendra'  not in s) #false
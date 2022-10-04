#creation  of tuple in different way
#creation of empty tuple
#Ex-1
t=()
print(t)
print(type(t))


#Ex-2
#Creation of tuple with single value
t=(23,)
print(t)
print(type(t))


#Ex-3
#creation of tuple with different data item
t=(23,'surendra',455.89,False)
print(t)

#Ex-4
#Creation of tuple without using ()
t=10,20,'laxmi',True,56.09
print(t)
print(type(t))


#Ex-5
#creation of tuple using tuple function
l=[10,20,30,40,50]
t=tuple(l) #list to tuple
print(t) #data in the form of tuple
print(l) #data in the form of list


#Ex-6
t=tuple(range(10))
print(t)

#Ex-7
t=tuple('Laxmipriya')
print(t)

# #Ex-8
# t=(10,20,30,40)
# t[1]=999
# print(t) #TypeError: 'tuple' object does not support item assignment

#Ex-9
t=(11,22,33,44)
print(t[2])

#Ex-10
t=(10,20,30,40,11,10,20,30)
print(t) #duplicate allowed

#Ex-11
t=(1,19,29,39,49)
print(t[-2]) #support -ve indexing

#Ex-12
#by using slice operator
t=(1,19,29,39,49)
print(t[::])
print(t[:2])
print(t[::2])

#Ex-13
#concatenation operation(+)
t=(10,20,30,40)
l=(11,22,33,44)
s=(25,35,45,55)
p=t+l+s
print(p)

#Ex-14
#Repetition operation
t=(10,20,30,40)
p=t*3
print(p)

#Ex-15
#traversing using for loop
t=(111,222,333,444,555,666)
for i in t:
    print(i)

#Ex-16
#Traversing using while loop
t=(111,222,333,444,555,666)
i=0
while i<len(t):
    print(t[i])
    i=i+1

#Tuple method

#index()
#Ex-17
t=(11,22,33,44,55)
print(t.index(44))

#count()
#Ex-18
t=(11,22,33,44,55,11)
print(t.count(11))

# #cmp()
# #Ex-19
# t1=(10,11)
# t2=(10,1)
# t3=(10,1)
# print(cmp(t1,t2)) #1 
# print(cmp(t2,t1))  #-1
# print(cmp(t2,t3))  # 0 #NameError: name 'cmp' is not defined

#len()
#Ex-20
t=(11,22,33,44,55,11)
print(len(t)) #6

#min() and max()
#Ex-21
t=(11,22,33,44,55,11)
print(min(t))
print(max(t))

#sorted() 
#Ex-22
t=(11,22,33,44,55,11)
e=sorted(t)
print(e) #sorted in ascending order #[11, 11, 22, 33, 44, 55]

#in descending order
#Ex-23
t=(11,22,33,44,55)
e=sorted(t,reverse=True)
print(e) #[55, 44, 33, 22, 11]

# Tuple packing and Tuple Unpacking

#packing (individual to group)
#Ex-24
a=99
b=45
c='Laxmi'
d=87.89
t=a,b,c,d #packing
print(t)
print(type(t)) #tuple

#Unpacking(group to individual)
#Ex-25
t=(99, 45, 'Laxmi', 87.89)
a,b,c,d=t
print(a,b,c,d)


#Ex-26
#Tuple for returning multiple values
def fun():
    l=[10,20,30,40,50,60]
    return(l[0],l[2],l[4])

t=fun()
print(t)    

#Ex-27
#Nested tuple
t=((23,'Laxmi',65.98),(78,'priyanka',35.98))
print(t)
print(t[0])
print(t[1])
print(t[0][1])
print(t[1][1])

#in loop
for i in t:
    print(i)

#Ex-28
#inside a tuple create a list
t=((23,'Laxmi',65.98),[78,'priyanka',35.98])
print(t[1])
t[1][1]='Madhu'
print(t[1])
print(type(t[1]))
print(t)

# #Ex-29
# #Tuple comprehension
# t=(i for i in range(10))
# print(t) #<generator object <genexpr> at 0x000001C1156A5EE0>
# print(type(t)) #<class 'generator'> #not possible

#Ex-30
t=tuple(i for i in range(10))
print(t) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(t)) #<class 'tuple'>


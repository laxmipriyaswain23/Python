#Ex-1
l=[i for i in range(11)]
print(l)

#Ex-2
l=[i*i for i in range(11)]
print(l)

#Ex-3
l=[i**i for i in range(11)]
print(l)

#Ex-4
l=[i+10 for i in range(11)]
print(l)


#Ex-5
l=[i for i in range(1,21)]
print(l)

#Ex-6
#using list comprehension
l=[i for i in range(1,21) if i%2==0]
print(l)

# #without using list comprehension
# l=[]
# for i in range(1,21):
#     if i%2==0:
#         l.append(i)

# print(l)        


# Ex-7
# name=['laxmi','rahul','zini','kabita']
# expected output:['l','r','z','k']

name=['laxmi','rahul','zini','kabita']
l=[i[0] for i in name]
print(l)

#Ex-8
#create a new list by adding the element which is containg letter a
name=['laxmi','rahul','zini','kabita']
l=[i for i in name if 'a' in i]
print(l)

#Ex-9
#create a new list add all the element if the element is rahul don't add instead of rahul add hlo
name=['laxmi','rahul','zini','kabita']
l=[i if i!='rahul' else 'hlo' for i in name]
print(l)

#Ex-10
#create a list from tuple
t=(10,20,30,40,50)
l=[i for i in t] 
print(l)


#Ex-11
t=(10,20,30,40,50)
l=[i for i in t if i%6==0] 
print(l)

#Ex-12
#create a list from a string
name='Laxmipriya'
l=[i for i in name]
print(l)

#Ex-13
#creation of matrix  using list comprehension
a=[[j for j in range(3)] for i in range(3)] #nested list
print(a)

#Ex-14
a=[[j for j in range(5)] for i in range(5)] 
print(a)

#Ex-15
a=[[i for j in range(3)] for i in range(3)] 
print(a)

#Ex-16
a=[[i*j for j in range(5)] for i in range(5)] 
print(a)
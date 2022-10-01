#using Equality operator
#Ex-1
l=['surendra','priyanka','rahul','zini']
p=['Surendra','Priyanka','Rahul','Zini']
s=['surendra','priyanka','rahul','zini']

print(l==s) #true
print(l==p) #false

#Ex-2
l=[10,20,30,40]
s=[10,20,30,40]
print(l !=s) #False

#Ex-3
l=[10,20,30,40,50]
s=[10,20,30,40]
print(l !=s) #true

#Ex-4
l=[10,20,30,40]
s=[20,30,40,10]
print(l ==s) #false bcz index in different order

#Using relational operator
#Ex-5
l=['surendra','priyanka','rahul','zini']
p=['Surendra','Priyanka','Rahul','Zini']
print(l>p) #true bcz s is greater than S
print(p>l) #false 

#Ex-6
a=[10,20,30]
b=[111]
print(a>b) #false 10 is not greater than 111

#Ex-7
a=[111]
b=[10,20,30]
print(a>b) #True 111 is greater than 10


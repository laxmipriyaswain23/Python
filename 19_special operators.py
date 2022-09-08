#Identity operator(is,is not)
#Ex-1
a=130
b=130 #bcz a and b are belonging from same memory location
print(a is b) #so we get true as result
print(id(a))
print(id(b))

#Ex-2
a=130
b=140 #bcz a and b are belonging from diffrent memory location
print(a is b) #so we get false as result
print(id(a))
print(id(b))

#ISnot operator
#Ex-3
a=130
b=130  
print(a is not b) #false bcz a is in b

#Ex-4
a=130
b=534  
print(a is not b) #true bcz a is not in b

#Ex-5
name='Harsh'
name1='Harsh'
print(name is name1) #True

#Ex-6
name='Harsh'
name1='Harsh'
print(name is not name1) #False

#Ex-7
name='Harsh'
name1='Rakshit'
print(name is name1) #false

#Ex-8
name='Harsh'
name1='Rakshit' 
print(name is not name1) #True

#Ex-9
a=True
b=True
print(a is b) #True

#Membership operators(in ,not in)
#Ex-10
name='laxmipriya swain'
print('a' in name) #True
print('aa' in name) #False
print('priya' in name) #True
print('' in name) #true
print('k'in name) #false
print('k' not in name) #true

#Ex-11
list=['rahul','priti','radha','ram','hari']
print('rahul' in list) #True
print('laxmi'not in list) #True
print('priti'not in list) #False
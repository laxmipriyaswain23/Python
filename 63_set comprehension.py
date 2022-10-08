#SET COMPREHENSION

#Ex-1
#create a set from list
l=[10,20,30,40]
s=set()
for i in l:
    s.add(i)

print(s)    


#using set comprehension
l=[10,20,30,40]
s={i for i in l}
print(s)


#Ex-2
l=[10,20,30,40]
s={i*2 for i in l}
print(s)


#Ex-3
#Create a set using range
s={i for i in range(100,111)}
print(s)



#Ex-4
s={i**2 for i in range(11)}
print(s)


#Ex-5
#create a set by adding all the element from 20 to 40 which is divisible by 4
s={i for i in range(20,41) if i % 4 == 0}
print(s)


#Ex-6
#create a set from a list called as names by adding the first character of each element
names=['surendra','priyanka','rahul']
s={i[0] for i in names}
print(s)


#Ex-7
#move the char to uppercase
names=['surendra','priyanka','rahul']
s={i[0].upper() for i in names}
print(s)

#Ex-8
#create a set from a list called as names by adding all the elements but if the element is priyanka the instead of priyanka add Laxmi
names=['surendra','priyanka','rahul','Pinky','kunal']
s={i if i!='priyanka' else 'laxmi'for i in names}
print(s)
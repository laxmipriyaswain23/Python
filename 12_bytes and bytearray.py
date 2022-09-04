a=[10,20,30,40] #list
#convert list to bytes
b=bytes(a)
print(b[0])
#print(b[4]) #index out of range
print(b[3])
print(b[-1])
print(b[-4])

for i in b:
    print(i)

#Byte Array
a=[10,20,30,40,50]
b=bytearray(a) #convert list to bytearray

#b=bytes(a) #u can't modify the value

print(b[1])
print(b[-1])
b[1]=200 #modify 1st index value
b[4]=240
for i in b:
    print((i))
#Ex-1
a=100
b=3
c=a/b
print(c)
print(type(c))

#Ex-2
x=10
y=10
z=x+y
print(z)
print(type(z))

#Ex-3
a=100
b=200.2
c=a+b
print(c)
print(type(c))
#other datatype to int
#float to int
a=int(45.90)
print(a)
b=int(34.67)
print(b)

#complex to int
# c=int(10+45j)
# print(c) #type Error

#bool to int
k=int(True)
print(k)
s=int(False)
print(s)
d=int(True+True+True+True)
print(d)
l=int(True+True-False)
print(l)

#str to int

# a=int('hello')
# print(a) #error

a=int('100')
print(a)

# b=int('10.20')
# print(b)  #float value is not possible only int value

# c=int('ob10101')
# print(c) #binary value is not possible 

#other datatype to float

#int to float
a=float(1000)
print(a)

#complex to float
# a=float(12+3j)
# print(a) #complex to float is not possible

#bool to float
a=float(True)
print(a)

b=float(True+True)
print(b)

a=float(False)
print(a)

#str to float
# a=float('hello')
# print(a) #value error not possible 

a=float('287')
print(a)

b=float('345.09')
print(b)

#Other datatype to complex

#int to complex
a=complex(10)
print(a)

#float to complex
a=complex(35.78)
print(a)

b=complex(23.87+45j)
print(b)

#bool to complex
a=complex(True)
print(a)

b=complex(False)
print(b)

c=complex(True+True+True)
print(c)
#str to complex

# a=complex('hello')
# print(a) #value error not possible

a=complex('34.89')
print(a)

b=complex(34)
print(b)

c=complex(10,2)
print(c)

d=complex(-45,-56)
print(d)

e=complex(True,False)
print(e)

s=complex(True,867)
print(s)

#Other to bool

#int to bool
a=bool(1)
print(a)

b=bool(12) 
print(b) #any non-zero value means true

b=bool(0)
print(b)
#float to bool
a=bool(10.0)
print(a)

b=bool(0.0)
print(b) #false we get as result

b=bool(0.1)
print(b) #non zero value so we get true

#complex to bool
a=bool(10+4j)
print(a)

a=bool(0+0j)
print(a) #False

#str to bool
a=bool('19')
print(a)

b=bool('hello')
print(b)

c=bool('')
print(c) #empty means false

a=bool('True')
print(a)

#Other to str
#int to str
a=str(10)
print(a)
print(type(a))

#float to int
a=str(10.87)
print(a)
print(type(a))

#complex  to str
a=str(10+6j)
print(a)
print(type(a))

#bool to str
a=str(False) # it converts to --'False' which is string
print(a)
print(type(a))

a=str(True)
print(a)
print(type(a))
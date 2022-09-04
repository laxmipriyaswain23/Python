msg="Welcome to kolkata"
print(msg[1:12:2])
print(msg[3:15:2])
print(msg[::])
print(msg[::2])
print(msg[::3])
print(msg[:4000:2])
# print(msg[100:14:2]) #we will get nothing (empty)
# #for backward traversing
print(msg[::-1])
print(msg[::-2])
# print(msg[-15:-14:-1]) #empty output
# print(msg[8:16:-1]) #empty output
print(msg[5000:2:-1])

c="My name is Laxmi"
print(c[-6::])
print(c[-1:-4:-1])
print(c[:-4:])
print(c[-4:-1:])
print(c[2:9])
print(c[2:])
print(c[::-+1])
print(c[1:-12:])
print(c[-2:-12:]) #empty
print(c[True:-1:1])
print(c[False+10:(True-True):-1])


#msg1="Hey i am here"
#print(msg1[1:9:1])
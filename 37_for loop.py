#for loop
#Ex-1
for i in range(10):
    print('Laxmi')

#Ex-2
for i in range(30):
    print('Laxmipriya')
    
#Ex-3
# 1 2 3 4 5 6 7 8 9 10
for i in range(1,11,1):
    print(i)    

#Ex-4
# 2 3 4 5 6 7 8
for i in range(2,9,1):
    print(i)    

#Ex-5
# 200 400 600 1000
for i in range(200,1200,200):
    print(i)    

#Ex-6
# 10 9 8  7 6 5 4 3 2 1
for i in range(10,0,-1):
    print(i)

#Ex-7
#999 777 555 333 111
for i in range(999,110,-222):
    print(i)

#Ex-8
#Print all even number from 100 to 120
for i in range(100,121,1):
    if i%2==0:
        print(i)

#OR
for i in range(100,121,2):
    print(i)        

#Ex-9
name='Laxmi priya swain'
for i in name:
    print(i)

#Ex-10
#name='55 55 55 55 5'
name='55 55 55 55 5'
for i in name:
    print(i)

#Ex-11
name='priyanka'
for i in name:
    print(i,end='-')

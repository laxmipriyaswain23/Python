#Program to search a value from a list then display its index,
# if the value is present multiple times then print its  all indices and
#  also count the number of times that value is repeated in the list
 

l=[10,20,30,40,50,10,20,30,40,50,10]
i=0
key=int(input("Hey plz enter a key:"))
count=0
while i<len(l):
    if key == l[i]:
        print(f'{key} is persent at {i} index')
        count=count+1
    i=i+1    
print(f'{key} is presnt {count} times')    

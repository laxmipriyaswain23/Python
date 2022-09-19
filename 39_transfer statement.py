# break,continue,pass

#Break
#Ex-1
for i in range(10):
    print(i)
    if i==7:
        break

#Ex-2
for i in range(10):
    if i==7:
        break
    print(i)    

#Continue means skip
#0 1 2  3 4 5 6 7 8 9
for i in range(10):
    if i==5:
       continue  #go back to the loop
    print(i)

#Pass -empty statement
#Ex-1
for i in range(10):
    if i%2==0:
        print(i) #print even number
    else:
        pass

#Ex-2
for i in range(10):
    if i%2==0:
        pass
    else:
        print(i)    #print odd number

#def f1():pass        
#Ex-1
#Input a student mark and check the result (pass or fail)
#mark>=33 pass otherwise fail
#using if

mark=int(input('enter your mark'))
if mark>=33:
    print('congratulation..pass')

if mark<33:
    print('sry.. fail')    

#Using if else
mark1=int(input('Enter ur mark')) 
if mark1>=33:
    print('cong..pass')  # condition is true thn if part execute
else:
    print('sry..fail') #condition false thn else part execute     

#Ex-2
num=int(input('Enter a number in between 1-5'))
if num==1:
    print('a')
elif num==2:
    print('b')
elif num==3:
    print('c') 
elif num==4:
    print('d')
elif num==5:
    print('e')
else:
    print('Invalid option plz enter a valid option')            

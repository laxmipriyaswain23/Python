#Wap to read the numbers until -1 is entered also count the negatives,positives and zeros entered by the users
num=int(input('Enter a number(if u want to exit plz enter -1)'))
npositive=0
nnegative=0
nzero=0
while num!=-1:
    if num>0:
        npositive=npositive+1
    elif num<0:
        nnegative=nnegative+1
    else:
        nzero=nzero+1  
    num=int(input('Enter a number(if u want to exit plz enter -1)'))          

print('Number of positive',npositive)
print('Number of negative',nnegative)
print('Number of zero',nzero)
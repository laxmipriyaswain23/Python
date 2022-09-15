#WAP  to enter the mark of a student in 6 subjects then calculate the total mark,avg mark and grade
#            avg>=90  ----->O grade
# avg>=80 and avg<=89 ------>E grade
# avg>=70 and avg<=79 ------>A grade
# avg>=60 and avg<=69 ------>B grade
# avg>=50 and avg<=59 ------>C grade
# avg<=40 and avg<=49 ------>D grade
# Otherwise Fail - Better Luck Next Time
phy=int(input('Enter phy mark'))
chem=int(input('Enter chem mark'))
bio=int(input('Enter bio mark'))
math=int(input('Enter math mark'))
eng=int(input('Enter eng mark'))
hindi=int(input('Enter hindi mark'))

print('----------')

totalmark=phy+chem+bio+math+eng+hindi
print('Totalmark is ',totalmark)

avgmark=totalmark/6
print('Avgmark is ',avgmark)

if avgmark>=90:
    print('O grade')
elif avgmark>=80 and avgmark<=89:
    print('E grade')    
elif avgmark>=70 and avgmark<=79:
    print('A grade') 
elif avgmark>=60 and avgmark<=69:
    print('B grade') 
elif avgmark>=50 and avgmark<=59:
    print('C grade') 
elif avgmark>=40 and avgmark<=49:
    print('D grade') 
else:
    print('Fail..Better luck next time')    
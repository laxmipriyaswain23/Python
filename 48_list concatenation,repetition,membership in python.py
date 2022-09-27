# #Ex-1
# #Concatenate
# l = ['laxmi','kamal',67,98,34]
# s = ['lucky','lopa',12,39,90]
# r=l+s
# print(r)

# # Ex-2
# a=[12,30,30.89,45,766]
# b=[122,33,567,678,789,543]
# c=[111,222,333,444,555,666,990]
# d=a+b+c
# print(d)

# #Ex-3
# a=[12,30,30.89,45,766]
# b=100
# d=a+b
# print(d) #type error

# #Ex-4
# a=[12,30,30.89,45,766]
# b=[100]
# d=a+b
# print(d)

# #Ex-5
# #Repetiton of lists
# l=[11,22,33,44,55]
# r=l*5
# print(r)

# #Ex-6
# l=[11,22,33,44,55]
# r=l*5.7
# print(r) #Type error

# #Ex-7
# l=[11,22,33,44,55]
# r=l*l
# print(r) #Type error

# #Ex-8
# #Membership in lists( in operator,not in operator)
# l=[10,20,30,40,50]
# print(20 in l)
# print(20 not in l)
# print(920 in l)
# print(45 not in l)

# #Ex-9
# #Wap to check whether your lucky number is present inside list or not
# l=[2,3,4,6,5,8,79,56,45,688,90,877,654,345,234]
# choice=int(input('Enter your lucky number:'))
# if choice in l:
#     print('Yes! ur lucky number is available')
# else:
#     print(' Sry Your! ur lucky number is not available')

#Ex-10
# Wap to check your lucky number until match your lucky number  with list element
l=[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,12,23,45]
choice=int(input('Enter ur lucky number:'))
while True:
    if choice in l:
        print('yes!! ur lucky number is available')
        break
    else:
        print('Sry!! u r lucky number is not available')
        choice=int(input('Enter u r lucky number:'))  

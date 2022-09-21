#Ex-1
l=[10,20,30,'survi','annika',45,679.90]
print(l)

#Ex-2
l=[10,20,30,'survi','annika',45,679.90]
print(l[4])
print(l[-3])


#CREATION OF LIST
#Ex-3
#CREATION OF EMPTY LIST
l=[]
print(l)

#Ex-4
#CREATION OF LIST DYNAMICALLIY USING eval() FUNCTION
l=eval(input('Enter a list'))
print(l)

#Ex-5
#CREATION OF LIST USING list() FUNCTION
l=list((23,67,89,657,356687))
print(l)

#Ex-6
#CREATION OF LIST USING range()
l=list(range(10,31))
print(l)

l=list(range(31))
print(l)

#Ex-7
#CREATION OF LIST DIRECTLY
l=[21,45,'kabir','Ash',8.8]
print(l)

#Ex-8
#list can hold complex datatype
k=[23,{"name":"Laxmipriya"},list((10,30,40))]
print(k)

#Ex-9
#use split() to create a list from a string
msg="My favo place is Simla"
l=msg.split()
print(l)

#Ex-10
msg="My-favo-plac-e-is-Sim-la"
l=msg.split('-')
print(l)

#Ex-11
msg="My favo place is Simla"
l=msg.split('l')
print(l)


#ACCESSING ELEMENTS OF LIST
#Ex-12
#Accessing Using index
l=[10,20,30,40,50,60]
print(l[1])
print(l[4])
print(l[-1])
print(l[-5])
#print(l[11]) #out of index

#Ex-13
#Accessing using slice operator
l=[97,56,87,92,56,89]
print(l[::])
print(l[2::2])


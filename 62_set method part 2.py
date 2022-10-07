#Set methods part 2

#Union()
#Ex-1
a={10,20,30,40}
b={56,58,69,79,30}
print(a.union(b))
print(a|b)

#intersection()
#Ex-2
A={10,20,30,40,50,60,70}
B={11,22,33,40,50,66,77}
print(A.intersection(B))
print(A & B)

#difference()
#Ex-3
A={11,22,33,44,55}
B={11,22,45,67}
print(A.difference(B))
print(B.difference(A))
print(A - B)
print(B - A)

#symmetric_difference()
#Ex-4
a={10,20,30,40}
b={11,20,30,44}
print(a.symmetric_difference(b))
print(a^b)


#issubset()
#Ex-5
a={1,2,3,4,5,6,7,8,9}
b={2,3,4,5}
print(b.issubset(a)) #true

#Ex-6
a={1,2,3,4,5,6,7,8,9}
b={22,33,44,55}
print(b.issubset(a)) #false
print(a.issubset(b)) #false

#issuperset()
#Ex-7
a={1,2,3,4,5,6,7,8,9}
b={2,3,4,5}
print(b.issuperset(a)) #false
print(a.issuperset(b)) #true

#disjoint()
#Ex-8
a={1,2,3,4,5,6,7}
b={10,20,30,40}
print(a.isdisjoint(b)) #true

#disjoint()
#Ex-9
a={1,2,3,4,5,6,7}
b={1,2,3,4}
print(a.isdisjoint(b)) #false
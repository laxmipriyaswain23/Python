#Creation of frozen set()

#Ex-1
s={10,2,30,40}
fs=frozenset(s)
print(fs) #frozenset({40, 10, 2, 30})
print(type(fs)) #<class 'frozenset'>

#Ex-2
#creation of frozenset from list
s=[10,2,30,40]
fs=frozenset(s)
print(fs) #frozenset({40, 10, 2, 30})
print(type(fs))

#Ex-3
#Creation of frozenset from range
fs=frozenset(range(10))
print(fs) #frozenset({40, 10, 2, 30})
print(type(fs))

# #Ex-4
# s={10,20,30,40,50,60}
# fs=frozenset(s)
# fs.add(888)
# print(fs) #AttributeError: 'frozenset' object has no attribute 'add'

# #Ex-5
# s={10,20,30,40,50,60}
# fs=frozenset(s)
# fs.remove(20)
# print(fs) #AttributeError: 'frozenset' object has no attribute 'remove'

#Ex-6
#Applying other normal method which will not modify frozenset

fs1=frozenset([1,2,4,7,89,45])
fs2=frozenset([1,22,33,44,55])
fs3=frozenset([23,45,1,22])
fs4=fs1.copy()
print(fs4)  #frozenset({1, 2, 4, 7, 45, 89})
print(fs1.union(fs2)) #frozenset({1, 2, 33, 4, 7, 44, 45, 22, 55, 89})
print(fs2.intersection(fs3)) #frozenset({1, 22})
print(fs1.difference(fs2)) #frozenset({2, 4, 7, 45, 89})
print(fs1.symmetric_difference(fs2)) #frozenset({2, 4, 7, 22, 89, 33, 44, 45, 55})
print(fs3.issubset(fs1)) #false
print(fs1.issuperset(fs3)) #false
print(fs1.isdisjoint(fs3)) #false

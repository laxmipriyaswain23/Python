#create a new list from a list 

#INPUT
#l=['Laxmi','Harsh','priti','sonu']

#OUTPUT
#['Li','Hh','Pi','Su']

l=['Laxmi','Harsh','priti','sonu']

new_list=[]

for i in l:
    new_list.append(i[0]+i[-1])
print(new_list)    

l=['Laxmi','Harsh','priti','sonu']

new_list=[]

for i in l:
    n=len(i)
    new_list.append(i[0]+i[n-1])
print(new_list)   
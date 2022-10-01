#INPUT
#a=['Hey','Hlo','Hy']
#b=['Laxmi','shivangi','Kajal','Priya']
#OUTPUT
#['Hey Laxmi','Hey shivangi','Hey kajal','Hey priya','Hlo Laxmi','Hlo shivangi','Hlo kajal','Hlo priya','Hy Laxmi','Hy shivangi','Hy kajal','Hy priya']


a=['Hey','Hlo','Hy']
b=['Laxmi','shivangi','Kajal','Priya']

nw_list=[]

for i in a:
    for j in b:
        nw_list.append(i+' '+j)

print(nw_list)        
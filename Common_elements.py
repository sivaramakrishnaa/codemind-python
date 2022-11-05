a,b = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

list_1 =[]
list_2 =[]

for i in l1:
    if i in l2 and i in l1:
        list_1.append(i)
for j in list_1:
    if j not in list_2:
        list_2.append(j)
print(*list_2)
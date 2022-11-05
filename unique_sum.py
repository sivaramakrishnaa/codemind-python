n = int(input())
l = list(map(int,input().split()))
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
s = 0   
for j in range(len(l1)):
    s += l1[j]
print(s)

m = int(input())
n = int(input())
c = 0
for i in range(m):
    l = list(map(int,input().split()))
    for j in range(len(l)):
        c += l[j]
print(c)
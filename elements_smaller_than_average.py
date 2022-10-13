n = int(input())
l = list(map(int,input().split()))
s = 0
for i in range(len(l)):
    s += l[i]
k = s // n
s1 = 0
for j in range (len(l)):
    if l[j] <= k:
        s1 += 1
print(s1)
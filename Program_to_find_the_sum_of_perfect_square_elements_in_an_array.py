import math
n = int(input())
l = list(map(int,input().split()))
c = 0
for i in l:
    t = math.sqrt(i)
    if t.is_integer():
        c += i
print(c)
        
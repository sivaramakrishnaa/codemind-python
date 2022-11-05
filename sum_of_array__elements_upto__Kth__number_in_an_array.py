n = int(input())
l = list(map(int,input().split()))
m = int(input())
s = 0
for i in l:
    s += int(i)
    if int(i) == m:
        break
print(s)
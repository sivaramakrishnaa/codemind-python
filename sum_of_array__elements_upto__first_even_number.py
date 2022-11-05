n = int(input())
l = list(map(int,input().split()))
s = 0
for i in l:
    if int(i) % 2 != 0:
        s += int(i)
    else:
        break
print(s)
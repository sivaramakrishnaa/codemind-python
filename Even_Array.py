n = int(input())
l = list(map(int,input().split()))

s = 0
for i in range(len(l)):
    if l[i] % 2 == 0:
        s += 1
        
if s == n:
    print('True')
else:
    print('False')
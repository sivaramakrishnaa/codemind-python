n = int(input())
l = list(map(int,input().split()))
s = 0
for i in l:
    if int(i) == 0 or int(i) == 1:
        s += 1
if len(l) == s:
    print('True')
else:
    print('False')
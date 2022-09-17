n = int(input())
l = list(map(int,input().split()))
s = int(input())
for i in l:
    if s == int(i):
        print('True')
        break
else:
    print('False')
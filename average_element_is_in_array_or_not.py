n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
k=s//n
for j in l:
    if j==k:
        print('True')
        break
else:
    print('False')
    
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=int(i)
print('%.2f'%round(s/n,2))
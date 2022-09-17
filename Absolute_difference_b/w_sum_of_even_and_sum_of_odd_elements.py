n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in l:
    if int(i)%2==1:
        s+=int(i)
    else:
        s1+=int(i)
print(abs(s-s1))
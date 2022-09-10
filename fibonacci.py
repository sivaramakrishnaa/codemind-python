n=int(input())
n1,n2=0,1
s=0
while s<n:
    print(n1,end=' ')
    nth=n1+n2
    n1=n2
    n2=nth
    s+=1
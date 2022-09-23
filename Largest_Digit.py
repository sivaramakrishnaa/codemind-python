n=int(input())
l=[]
while n>0:
    k=n%10
    l.append(k)
    n=n//10
print(max(l))
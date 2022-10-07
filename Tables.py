a,b=map(int,input().split())
for i in range(1,b+1):
    if i % 2 == 0:
        continue
    c = i*a
    print(a,"x",i,"=",c)
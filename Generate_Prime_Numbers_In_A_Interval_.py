a=int(input())
b=int(input())
for j in range(a,b+1):
    s=0
    for i in range (1,j+1):
        if j % i == 0:
            s += 1
    if s == 2:
        print(j)
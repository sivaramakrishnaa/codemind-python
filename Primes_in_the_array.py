n = int(input())
l = list(map(int,input().split()))
s1 = 0

for i in range(len(l)):
    
    s = 0
    for j in range(1,l[i]+1):
        if l[i] % j == 0:
            s +=1
    if s == 2:
        s1 += 1
print(s1)
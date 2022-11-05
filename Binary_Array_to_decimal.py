n = int(input())
l = list(map(int,input().split()))

rev = l[::-1]

s1=0
s2=0
for i in rev:
    s1 += (2**s2) * (int(i))
    s2 += 1
    
print(s1)
    
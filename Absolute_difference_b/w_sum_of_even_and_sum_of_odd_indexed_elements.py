n = int(input())
l = list(map(int,input().split()))
s = 0
s1 = 0
for i in range ( len(l) ):
    if i % 2 == 1:
        s += l[i]
    else:
        s1 += l[i]
print( abs ( s-s1 ) )
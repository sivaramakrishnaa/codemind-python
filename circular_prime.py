n = str(input())
 
k = n[::-1]

s = 0
for i in range(1,int(n)+1):
    if int(n) % i == 0:
        s += 1
s1 = 0
for j in range(1,int(k)+1):
    if int(k) % j == 0:
        s1 += 1
if s == 2 and s1 == 2:
    print('circular prime')
elif s == 2 and s1 != 2:
    print('prime but not a circular prime')
else:
    print('not prime')
        
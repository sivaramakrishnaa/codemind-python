n = int(input())
s1 = 1
for i in range(1,n+1):
    if n % i == 0:
        prime = True
        for j in range(2,i):
            if i % j == 0:
                prime = False
        if prime == True:
            continue
        s1 += 1
print(s1)
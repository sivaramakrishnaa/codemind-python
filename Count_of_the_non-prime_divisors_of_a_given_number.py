n = int (input())

s1 = 0
for i in range(1,n+1):
    if n % i == 0:
        
        s = 0
        for j in range(1,i+1):
            if i % j == 0:
                s += 1
                
        if s == 2:
            continue
        s1 += 1
print(s1)
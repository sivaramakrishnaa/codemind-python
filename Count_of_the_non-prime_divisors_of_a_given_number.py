n = int(input())

s1 = 0

for i in range(1,n+1):
    if n % i == 0:
        t = i
        
        s2 = 0
        for j in range(1,t+1):
            if t % j == 0:
                s2 += 1
        if s2 == 2:
            continue
        s1 += 1
print(s1)
    
            
            
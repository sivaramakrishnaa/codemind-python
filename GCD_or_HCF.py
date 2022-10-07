a,b = map(int,input().split())

k = max(a,b)

var = 0

for i in range(1,k+1):
    if a % i == 0 and b % i == 0:
        var = i
print(var)
        

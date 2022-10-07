a,b = map(int,input().split())

var = 0
 
k = max(a,b)

for i in range(1, k+1):
    if a % i == 0 and b % i == 0 :
        var = i
print(var)
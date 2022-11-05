y = int(input())

n = y + 1

while 1:
    prime = 0
    for i in range(2,n):
        if n % i == 0:
            prime = 1
            break
    x = n
    rev = str(x)[::-1]
    
    if int(rev) == int(x) and prime == 0:
        print(n)
        break
    else:
        n = n +1
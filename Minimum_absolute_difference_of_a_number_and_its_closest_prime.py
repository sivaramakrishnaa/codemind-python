a = int(input())
j = a
while 1:
    n = j
    isprime = True
    for i in range(2, j):
        if n % i == 0:
            isprime = False
            break
    if isprime == True:
        break
    else:
        j -= 1

k = a
while 1:
    m = k
    isprime = True
    for z in range(2, k):
        if m % z == 0:
            isprime = False
            break
    if isprime == True:
        break
    else:
        k += 1     
o = abs(a-n)
p = abs(a-m)
print(min(o,p))
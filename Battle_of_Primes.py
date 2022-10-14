a = int(input())
b = int(input())
c = a + b

s = 1

z = c + 1
while 1:
    y = z
    isprime = True
    for i in range(2,z):
        if y % i == 0:
            isprime = False
            break
    if isprime == True:
        print(s)
        break
    else:
        z += 1
        s += 1
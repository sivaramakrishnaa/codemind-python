n = int(input())

k = n * n

ln_1 = len(str(k))
ln_2 = len(str(n))

x = str(k)[(ln_1-ln_2):]

if int(x) == int(n) :
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
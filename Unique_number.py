n = int(input())
a = []
s = 0
while n > 0:
    s +=1
    k = n % 10
    if k not in a:
        a.append(k)
    n = n //10
if s== len(a):
    print('Unique Number')
else:
    print('Not Unique Number')
n = int(input())
a = []
size = 0
while n > 0:
    size += 1
    k = n % 10
    if k not in a:
        a.append(k)
    n = n //10
if size == len(a):
    print('Unique Number')
else:
    print('Not Unique Number')
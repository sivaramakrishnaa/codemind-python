n = int(input())
x = n
while x >= 10:
    s = 0
    while x > 0:
        rem = x % 10
        s += rem**2
        x = x//10
    x = s
if x == 1 or x == 7:
    print('True')
else:
    print('False')
a,b = map(int,input().split())
i = 1
while True:
    c = a * i
    if c % b == 0:
        print(c)
        break
    i += 1
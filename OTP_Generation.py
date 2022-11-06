n = input()

s = ''
for i in n:
    if int(i) % 2 == 1:
        k = int(i)**2
        k = str(k)
        s = s+k
print(s)
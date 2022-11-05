n = int(input())

while 1:
    rev1 = str(n)[::-1]
    m = n + int(rev1)
    
    rev = str(m)[::-1]
    
    if m == int(rev):
        print(m)
        break
    else:
        n = n + int(rev1)
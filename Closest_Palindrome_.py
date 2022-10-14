n = int(input())

y = n + 1
while 1:
    s = str(y)
    rev = s[::-1]
    if int(s) == int(rev):
        
        break
    else:
        y += 1
       
z = n - 1
while 1:
    t = str(z)
    ver = t[::-1]
    if int(t) == int(ver):    
        
        break
    else:
        z -= 1
if abs(int(s) - n) < abs(int(t) - n):
    print(int(s))
elif abs(int(s) - n) == abs(int(t) - n):
    print(int(t),int(s))
else:
    print(int(t))
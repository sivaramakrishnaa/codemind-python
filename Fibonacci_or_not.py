n = int(input())
a=[]
s = 0
n1,n2 = 0,1
while s < n:
    a.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    s += 1
if n in a:
    print('True')
else:
    print('False')
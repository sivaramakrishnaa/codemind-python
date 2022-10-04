a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    rev = 0
    while  i> 0:
        r = i % 10 
        rev = rev * 10 + r 
        i = i // 10 
    if t == rev:
        print(t,end =' ')
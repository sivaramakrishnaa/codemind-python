t=int(input())
for i in range(t):
    a=str(input())
    n=a[::-1]
    if n==a:
        print('True')
    else:
        print('False')
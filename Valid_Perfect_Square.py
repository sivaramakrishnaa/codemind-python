t=int(input())
for i in range(t):
    a=int(input())
    z= a**(0.5)
    if a%z==0:
        print('True')
    else:
        print('False')
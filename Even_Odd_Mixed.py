n=int(input())
s=0
s1=0
while n > 0:
    r = n % 10
    if r%2==1:
        s+=1
    else:
        s1+=1
    n=n//10
if s==0 and s1>0 :
    print('Even')
elif s>0 and s1==0:
    print('Odd')
else:
    print('Mixed')
            
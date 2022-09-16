n=int(input())
s=0
s1=1
while n>0:
    k=n%10
    s+=k
    s1 *=k
    n //=10
if s==s1:
    print('Spy Number')
else:
    print('Not Spy Number')
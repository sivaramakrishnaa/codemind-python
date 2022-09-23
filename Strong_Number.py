n=int(input())
s=0
for i in str(n):
    s1=1
    for k in range(1,int(i)+1):
        s1 *=k
    s+=s1
if int(n)==s:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")
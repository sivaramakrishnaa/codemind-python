n = int(input())
s = 1
s1 = 0 
while n > 0:
    k = n % 10
    s *= k
    s1 += k
    n=n//10
print(s-s1)
    
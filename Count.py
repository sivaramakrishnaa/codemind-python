n = int(input())
lst = list(map(int,input().split()))
count1,count2 = 0,0
for num in lst:
    if num % 2 == 0:
        count1 += 1
    else:
        count2 += 1
print(count1,count2)

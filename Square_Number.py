n = int(input())
for i in range(n):
    sq = i*i
    if sq == n:
        print('True')
        break
else:
    print('False')
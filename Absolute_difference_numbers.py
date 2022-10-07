a,b = map(int,input().split())
length = len(str(a))
ind_1=str(a)[length-b:]
ind_2=str(a)[:b]
total=abs(int(ind_1)-int(ind_2))
print(total)
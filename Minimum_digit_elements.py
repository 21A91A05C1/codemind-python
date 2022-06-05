n=int(input())
l=list(map(int,input().split()))
min=999
c=0
for i in range(len(l)):
    if len(str(l[i]))<min:
        min=len(str(l[i]))
for i in range(len(l)):
    if len(str(l[i]))==min:
        c+=1
print(c)
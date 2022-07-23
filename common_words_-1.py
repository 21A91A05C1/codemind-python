s=list(map(str,input().lower().split()))
p=list(map(str,input().lower().split()))
c=0
for i in s:
    if i in p:
        c+=1
print(c)
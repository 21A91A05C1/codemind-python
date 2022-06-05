l=list(map(str,input().lower().split()))
m=list(map(str,input().lower().split()))
c=0
for i in l:
    if i in m:
        c+=1
print(c)

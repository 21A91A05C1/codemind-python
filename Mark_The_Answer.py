n,m=map(int,input().split())
k=list(map(int,input().split()))
d=0
c=0
for i in k:
    if d<=1 and i<=m:
            c+=1
    else:
        d+=1
    
print(c)


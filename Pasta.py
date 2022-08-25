n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in b:
    if i in a:
        if b.count(i)<=a.count(i):
            c+=1
if(c==m):
    print("Yes")
else:
    print("No")
    

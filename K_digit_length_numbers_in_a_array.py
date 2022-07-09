n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l[i]>=0:
        if( len(str(l[i]))==m):
            c+=1
    else:
        if(len(str(l[i]))==m+1):
            c+=1
print(c)
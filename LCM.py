n,m=map(int,input().split())
for i in range(1,n+1) and range(1,m+1):
    if(n%i==0 and m%i==0):
        res=i
k=(n*m)/res
print("%d"%k)
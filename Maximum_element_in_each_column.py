n,m=map(int,input().split())
max=-9999
a=[list(map(int,input().split()))
for i in range(n)]
for j in range(m):
    max=-9999
    for i in range(n):
        if(max<a[i][j]):
            max=a[i][j]
    print(max)
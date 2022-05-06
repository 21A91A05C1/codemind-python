t=int(input())
while(t!=0):
    n,m=map(int,input().split())
    ans=-1
    for i in range(0,m+1):
        if((i*i)%m==n):
            ans=i
            break
    print(ans)
    t=t-1
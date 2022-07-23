t=int(input())
while(t!=0):
    n=int(input())
    p=list(map(int,input().split()))
    s=0
    u=0
    flag=0
    for i in range(len(p)):
        s=sum(p[:i])
        l=sum(p[i+1:])
        if s==l:
            flag=1
            break
    if flag==1:
        print("YES")
    else:
        print("NO")
    t-=1
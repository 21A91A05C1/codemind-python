t=int(input())
while(t!=0):
    c=0
    n,m=map(int,input().split())
    for i in range(n,m+1):
        if(i%10==2 or i%10==3 or i%10==9):
            c=c+1
    print(c)
    t=t-1
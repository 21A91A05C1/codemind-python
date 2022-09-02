t=int(input())
while(t!=0):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(0,len(l)):
        s=0
        c=0
        for j in range(i,len(l)):
            s=s+l[j]
            #print(s)
            if s==m:
                print(i+1,j+1)
                c+=1
        if(c>0):
            break
    if(c==0):
        print(-1)
    t-=1
t=int(input())
while(t!=0):
    c=1
    n=int(input())
    k=list(map(int,input().split()))
    for i in range(0,len(k)-1):
        if k[i]>k[i+1]:
            c+=1
    print(c)
    t-=1
    
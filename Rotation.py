t=int(input())
while(t!=0):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    k=[]
    for i in range(len(arr)):
        k.append(arr[(n-m+i)%n])
    print(*k)
    t-=1
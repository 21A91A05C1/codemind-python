t=int(input())
while t!=0:
    n=int(input())
    arr=list(map(int,input().split()))
    l=[]
    arr=sorted(arr)
    i=-1
    j=0
    c=0
    while(c<len(arr)):
        if arr[i] not in l:
            l.append(arr[i])
        if arr[j] not in l:
            l.append(arr[j])
        i=i-1
        j=j+1
        c=c+2
    print(*l)
    t-=1
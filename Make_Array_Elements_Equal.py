n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
c=p=0
if len(k)==1:
    print(0)
else:
    for i in range(n):
        c=0
        for j in range(i,n):
            if l[i]==l[j]:
                c+=1
        if p<c:
            p=c
    print(p)   
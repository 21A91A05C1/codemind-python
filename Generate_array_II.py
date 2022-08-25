n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,len(l),2):
    while(l[i+1]):
        k.append(l[i])
        l[i+1]-=1
print(*k)
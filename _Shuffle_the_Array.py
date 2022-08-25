n=int(input())
l=list(map(int,input().split()))
k=[]
m=n//2
for i in range(m):
    k.append(l[i])
    k.append(l[i+m])
print(*k)
    
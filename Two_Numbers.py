n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in arr:
    if arr.count(i)!=2:
        k.append(i)
print(*sorted(k))
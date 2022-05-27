n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in arr:
    k.append(i*i)
p=sorted(k)
print(*p)
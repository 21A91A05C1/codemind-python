l=int(input())
n=list(map(int,input().split()))
k=[]
for i in range(len(n)):
    max=-1
    for j in range(i+1,len(n)):
        if n[j]>max:
            max=n[j]
    k.append(max)
print(*k)
        
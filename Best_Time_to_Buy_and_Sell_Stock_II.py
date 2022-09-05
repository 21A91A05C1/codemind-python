n=int(input())
k=list(map(int,input().split()))
s=0
for i in range(len(k)-1):
    if (k[i]<k[i+1]):
        s=s+(k[i+1]-k[i])
print(s)
n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if(l[i]%2==0):
        s=s+l[i]
print(s)
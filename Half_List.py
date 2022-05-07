n=int(input())
m=list(map(int,input().split()))
for i in range(n-1,(n//2)-1,-1):
    print(m[i],end=" ")
for i in range(0,n//2):
    print(m[i],end=" ")
n=int(input())
arr=list(map(int,input().split()))
r=int(input())
r=r%n
if(r==0):
    print(*arr)
else:
    print(*arr[-r:]+arr[:n-r])
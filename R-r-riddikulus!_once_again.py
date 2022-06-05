n,r=map(int,input().split())
arr=list(map(int,input().split()))
r=r%n
r=abs(r-n)
if(r==0):
    print(arr)
else:
    print(*(arr[-r:])+(arr[:n-r]))
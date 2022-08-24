n=int(input())
arr=list(map(int,input().split()))
m=int(input())
brr=list(map(int,input().split()))
l=int(input())
c=0
for i in range(n):
    if(l>=arr[i] and l<=brr[i]):
        c=c+1
print(c)
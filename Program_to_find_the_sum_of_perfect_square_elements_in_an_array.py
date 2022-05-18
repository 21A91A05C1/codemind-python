n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    for j in range(1,10):
        if(a[i]==j**2):
            sum=sum+a[i]
print(sum)
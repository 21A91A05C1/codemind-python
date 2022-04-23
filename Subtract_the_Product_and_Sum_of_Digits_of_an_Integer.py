n=int(input())
sum=0
res=1
while(n!=0):
    d=n%10
    sum=sum+d
    res=res*d
    n=n//10
print(res-sum)



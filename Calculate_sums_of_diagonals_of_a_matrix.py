a=int(input())
sum=0
sum1=0
for i in range(a):
    arr=list(map(int,input().split()))
    for j in range(a):
        if(i==j):
            sum=sum+arr[j]
        if(i+j==a-1):
            sum1=sum1+arr[j]
print("Principal Diagonal:",end="")
print(sum)
print("Secondary Diagonal:",end="")
print(sum1)
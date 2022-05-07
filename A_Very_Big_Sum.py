n=int(input())
sum=0
m=list(map(int,input().split()))
for i in range(len(m)):
    sum=sum+m[i]
print(sum)
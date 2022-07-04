n=int(input())
l=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(len(l)):
    if l[i]==k:
        sum+=1
print(sum)
n=int(input())
flag=0
i=1
for i in range(1,n):
    if(n==i*i+1):
        flag=1
if(flag==1):
    print("NO")
else:
    print("YES")    
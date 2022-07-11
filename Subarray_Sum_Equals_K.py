n,k=map(int,input().split())
arr =list(map(int,input().split()))
res = 0
for i in range(n):
    sum= 0           
    for j in range(i, n):
        sum+= arr[j]
        if sum== k:
            res += 1
print(res)
n=int(input())
s=0
max=-999999
arr=list(map(int,input().split()))
#print(arr)
for i in range(len(arr)):
    s=0
    s=s+arr[i]
    for j in range(i+1,len(arr)):
        s=s+arr[j]
        if s>max:
            max=s
'''
this down part is because we may have a single number
having maximum then all the sub arrays
check by printing arr second test case is the example for it
'''
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)
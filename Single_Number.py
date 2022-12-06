n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
#print(arr)
for i in range(0,len(arr)-1,2):
    if(arr[i]!=arr[i+1]):
        print(arr[i])
        break
else:
    print(arr[-1])
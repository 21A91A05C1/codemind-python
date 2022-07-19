arr=input()
c=0
d=0
for i in range(len(arr)):
    c=0
    for j in range(i,len(arr)-1):
        if arr[j]==arr[i] and arr[j+1]==arr[i] and i>0:
            c+=1
            if d<c:
                d=c
        else:
            break
print(d+1)
arr=input()
c=0
d=0
v="aeiouAEIOU"
for i in range(len(arr)):
    c=0
    for j in range(i,len(arr)):
        if arr[j] in v:
            c+=1
            if d<c:
                d=c
        else:
            break
print(d)
n=(input()).lower()
arr=[]
for i in n:
    if i==" ":
        continue
    else:
        if i not in arr:
            arr.append(i)
k=sorted(arr)
print("".join(k))
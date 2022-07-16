s1=input().lower()
s2=input().lower()
a1=""
a2=""
arr=[]
for i in s1:
    if i.isspace():
        continue
    else:
        a1=a1+i
for i in s2:
    if i.isspace():
        continue
    else:
        a2=a2+i
for i in a1:
        if i not in a2:
            if i not in arr:
                arr.append(i)
for j in a2:
    if j not  in a1:
        if j not in arr:
            arr.append(j)
k=sorted(arr)
print("".join(k))
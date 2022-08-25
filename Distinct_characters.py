n=input().lower()
l=[]
for i in n:
    if n.count(i)==1:
        if i!=" ":
            l.append(i)
l=sorted(l)
print("".join(l))
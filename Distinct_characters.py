n=input().lower()
k=set(n)
l=(sorted(k))
#print(sorted(k))
p=""
for i in l:
    if i==' ':
        continue
    else:
        p=p+i
print(p)
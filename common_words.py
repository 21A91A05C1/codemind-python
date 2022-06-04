s=list(map(str,input().lower().split()))
l=list(map(str,input().lower().split()))
k=[]
for i in l:
    if i in s:
        k.append(i)
print (*k)
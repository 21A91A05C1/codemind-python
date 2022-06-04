n=list(map(str,input().split()))
k=[]
l="aeiouAEIOU"
for i in n:
    c=0
    for j in range(len(i)):
        if i[j] in l:
            c+=1
    k.append(c)
print(max(k))

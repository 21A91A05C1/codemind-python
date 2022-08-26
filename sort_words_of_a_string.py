n=input().split(" ")
l=[]
for i in n:
    r=""
    p=""
    c=""
    for j in i:
        if j.isalpha():
            r=r+j
        else:
            c=c+j
    r=sorted(r)
    k=0
    t=0
    for j in i:
        if j.isalpha():
            p=p+r[k]
            k+=1
        else:
            p=p+c[t]
            t+=1
    l.append(p)
print(*l)
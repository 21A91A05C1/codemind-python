q=input()
n=q.split()
#print(n)
p=[]
m=""
for i in n:
    k=[]
    for j in i:
        if j.isalpha():
            k.append(j)
    k=sorted(k)
    #print(k)
    h=0
    m=""
    for o in range(len(i)):
        if i[o].isalpha():
            m=m+k[h]
            h+=1
        else:
            m=m+i[o]
    p.append(m)
print(*p)
            
n,m=map(str,input().split())
m=list(m)
c=0
for i in n:
    for j in i:
        if j in m:
            m.remove(j)
            c+=1
        else:
            break
if c==len(n):
    print("True")
else:
    print("False")
        
n=list(map(str,input().split()))
#print(n)
k="aeiouAEIOU"
u=[]
d=1
min=100
for i in n:
    c=0
    for j in i:
        if j in k:
            c+=1
    u.append(c)
    if(c<min):
        min=c
    elif(c==min):
        d+=1
print(d)
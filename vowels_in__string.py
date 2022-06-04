n=input()
k="aeiouAEIOU"
p=[]
for i in n:
    if i in k:
        if i not in p:
            p.append(i)
if(len(p)!=0):
    print(*p)
else:
    print("-1")
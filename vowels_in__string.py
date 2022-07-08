n=input()
k="aeiouAEIOU"
p=[]

for i in range(len(n)):
    if n[i] in k:
        if  n[i] not in p:
            p.append(n[i])
if(len(p)==0):
    print("-1")
print(*(p))
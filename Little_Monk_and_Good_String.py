n=(input())
c=0
d=0
v="aeiouAEIOU"
for i in range(len(n)):
    c=0
    for j in range(i,len(n)):
        if n[j] in v:
            c+=1
            if c>d:
                d=c
        else:
            break
print(d)
        
l=list(map(str,input().split()))
p="aeiouAEIOU"
c=0
for i in l:
    if i[0] in p and i[-1] not in p:
        c+=1
print(c)
    
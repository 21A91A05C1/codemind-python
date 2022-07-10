n=list(map(str,input().split()))
c=0
for i in n:
    if(i[0] in "aeiouAEIOU" and i[-1] not in "aeiouAEIOU"):
        c+=1
print(c)

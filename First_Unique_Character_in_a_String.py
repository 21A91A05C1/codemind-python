s=input()
c=0
p=0
ind=0
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if(i!=j):
            if(s[i]==s[j]):
                c+=1
    if(c!=0):
        continue
    else:
        ind=i
        p+=1
        break
if(p==0):
    print(-1)
else:
    print(ind)
    
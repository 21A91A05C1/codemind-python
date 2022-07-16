n=(input()).lower()
c=0
d=0
for i in n:
    c=0
    if i==" ":
        continue
    else:
        for j in n:
            if i==j :
                c+=1
        if(c==1):
            d+=1
print(d)
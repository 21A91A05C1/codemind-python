n=(input()).lower()
a=[]
for i in n:
    if i==" ":
        continue
    else:
        if i not in a:
            a.append(i)
print(len(a))
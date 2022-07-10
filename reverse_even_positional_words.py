n=input()
k=n.split()
p=[]
for i in range(len(k)):
    if i%2==0:
        p.append(k[i][::-1])
    else:
        p.append(k[i])
print(*p)
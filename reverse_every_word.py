n=input()
k=n.split()
p=[]
for i in k:
    p.append(i[::-1])
print(' '.join(p))
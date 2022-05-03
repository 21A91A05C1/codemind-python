n=input()
w=n.split()
z=[]
for i in w:
    z.append(i[::-1])
print(" ".join(z))
n=input()
k="aeiou"
p=[]
flag=0
for i in n:
    if i in k:
        p.append(i)
z=set(p)
if(len(k)==len(z)):
    print("True")
else:
    print("False")
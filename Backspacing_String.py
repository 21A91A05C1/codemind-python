s=input()
t=input()
k=[]
n=[]
for i in s:
    if i=='#':
        k.pop()
    else:
        k.append(i)
for i in t:
    if i=='#':
        n.pop()
    else:
        n.append(i)
if(k==n):
    print("True")
else:
    print("False")
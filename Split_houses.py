n=int(input())
s=input()
k=""
c=0
for i in s:
    if i==".":
        k=k+'B'
    else:
        k=k+i
for i in range(len(k)-1):
    if k[i]==k[i+1]=='H':
        c+=1
if (c==0):
    print("YES")
    print(k)
else:
    print("NO")
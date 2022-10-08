n=input()
s=""
k=[]
for i in range(len(n)):
    s=""
    for j in range(i,len(n)):
        if((n[j].upper() not in s) and (n[j].lower() not in s)):
            s=s+n[j]
        else:
            break
    k.append(s)
max=0
for i in k:
    if len(i)>max:
        max=len(i)
flag=0
if(max<3):
    print(-1)
    flag=1
for i in k:
    if len(i)==max and flag==0:
        print(i)
        break
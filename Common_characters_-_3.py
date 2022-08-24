n=input().lower().split(" ")
a=n[0]
c=0
s=''
for i in a:
    c=0
    for j in range(1,len(n)):
        if i in n[j]:
            c+=1
    if(c==len(n)-1):
        s=s+i
if(len(s)!=0):
    print(min(s))
else:
    print("-1")
    
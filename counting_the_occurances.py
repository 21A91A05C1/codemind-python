n=input()
k=input()
c=0
flag=0
for i in n:
    if(i==k):
        c=c+1
        flag=1
if(flag==1):
    print(c)
else:
    print("-1")
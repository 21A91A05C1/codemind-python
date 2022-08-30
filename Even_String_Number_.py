n=input()
k="789654123"
l=[]
for i in n:
    if i in k:
        l.append(i)
l=set(l)
c=0
for i in l:
    if(int(i)%2==0):
        c+=1
if c==0:
    print('-1')
else:
    l=sorted(l)
    l=l[::-1]
    for i in l:
        if(int(i)%2==0):
            e=i
    for i in l:
        if i!=e:
            print(i,end="")
    print(e)
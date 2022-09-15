n=int(input())
a=0
b=1
k=[]
l=[]
i=0
max=999
maxx=0
k.append(a)
while(i!=n):
    c=a+b
    a=b
    b=c
    k.append(c)
    i+=1
#print(k)
for i in range(len(k)):
    if(abs(k[i]-n)<max):
        max=abs(k[i]-n)
        maxx=k[i]
        #print(max,end=" ")
        #print(maxx)
    elif(abs(k[i]-n)==max):
        l.append(k[i])
print(maxx,*l)
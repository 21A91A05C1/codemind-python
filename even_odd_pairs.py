n=int(input())
p=list(map(int,input().split()))
k=[]
u=[]

for i in p:
    if i%2==0:
        k.append(i)
    else:
        u.append(i)
i=0
j=0
while(i<len(u) or j<len(k)):
    if j<len(k):
        print(k[j],end=" ")
        j+=1
    if i<len(u): 
        print(u[i],end=" ")
        i+=1
if(n%2==1):
    print("0")

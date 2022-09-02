n,p,q=map(int,input().split())
arr=list(map(int,input().split()))
k=[]
while(q!=0):
    r=int(input())
    #print(r)
    k.append(r)
    q-=1
#print(k)
z=[]
for i in range(len(arr)):
    z.append(arr[(n-p+i)%n])
#print(z)
f=[]
for i in range(len(k)):
    print(z[k[i]])
#print(f,end="
")
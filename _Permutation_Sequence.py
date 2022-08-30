from itertools import permutations
n,m=map(int,input().split())
k=''
l=[]
for i in range(1,n+1):
    k=k+str(i)
#print(k)
for i in permutations(k):
    l.append(i)
#print(l) 
for i in range(0,len(l)):
    if(i==m-1):
        #print(i)
        print("".join(l[i]))
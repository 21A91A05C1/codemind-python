n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=0
s=0
for i in  l:
    s=s+i
for j in m:
    k=k+j
if((k-s)>0):
    print(k-s)
else:
    print("0")    
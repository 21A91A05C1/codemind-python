l=list(map(str,input().split()))
k=[]
for i in range(len(l)):
    k.append(len(l[i]))
    
print(max(k))
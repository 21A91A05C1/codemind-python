l=list(map(str,input().split()))
k=[]
for i in range(len(l)):
    if i%2==0:
        k.append((l[i][::-1]))
    else:
        k.append(l[i])
print( *k)
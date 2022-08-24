n=list(map(str,input().split()))

for i in range(len(n)):
    for j in range(0,len(n)):
        if(len(n[i])<len(n[j]) and i!=j):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print( *n)



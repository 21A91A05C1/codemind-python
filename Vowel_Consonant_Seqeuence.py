n=input()
k=""
l=""
for i in n:
    if i in 'aeiou':
        k=k+'V'
    else:
        k=k+'C'
#print(k)
i=1
m=k[0]
for i in range(1,len(k)):
    if(m==k[i]):
        continue
    else:
        l=l+m
        m=k[i]
l=l+k[-1]
print(l)
        
    
        
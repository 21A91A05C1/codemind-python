n=list(map(str,input().split()))
k=n[-1]
p=min(k)
#print(k)
#print(p)
if p.lower()  in k:
    print(p.lower())
else:
    print(p)
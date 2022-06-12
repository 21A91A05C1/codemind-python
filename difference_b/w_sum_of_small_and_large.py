l=list(map(str,input().split()))
k=0
p=0
for i in l:
    k=k+ord(min(i))
    p=p+ord(max(i))
print(abs(k-p))
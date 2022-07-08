n=list(map(str,input().lower().split()))
c=0
for i in range(len(n)):
    if n[i]==n[i][::-1]:
        c+=1
print(c)
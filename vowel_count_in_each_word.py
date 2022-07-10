l=list(map(str,input().split()))
for i in l:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    print(c,end=" ")
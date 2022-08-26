n=int(input())
c=0
while n:
    k=input()
    for i in range(len(k)):#range ae number ichina same
        if k[i]=='+':
            c+=1
            break
        elif k[i]=='-':
            c-=1
            break
        
    n-=1
print(c)

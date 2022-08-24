n=input().lower().split(" ")
c=0
p="aeiou"
for i in n:
    l=0
    k=len(i)-1
    while l<k:
            if((i[l] in p and i[k] not  in p ) or (i[l] not  in p and i[k] in p )):
                c+=1
            l+=1
            k-=1
print(c)
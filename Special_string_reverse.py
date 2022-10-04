n=input()
k=""
l=""
for i in n:
    if i.isalpha():
        k=k+i
k=k[::-1]
j=0
for i in n:
    if i.isalpha():
        l=l+k[j]
        j+=1
    else:
        l=l+i
print(l)
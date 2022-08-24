n=input().lower()
n=n.replace(" ","")#should keep hidden is failing otherwise
c=0
for i in n:
    if n.count(i)==1:
        c+=1
print(c)

n=input().lower()
s=''
c=0
for i in n:
    if(n.count(i)==1):
        s=s+i
s=list(s)
s.sort()
s=str(s)
s=s.replace(" ","")
s=s.replace("'","")
s=s.replace(",","")
s=s.replace("[","")
s=s.replace("]","")
print(s)
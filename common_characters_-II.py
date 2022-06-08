n=input().lower()
s=input().lower()
n=set(n)
s=set(s)
c=0
for i in n:
    if i in s and i!=" ":
        c+=1
print(c)
    
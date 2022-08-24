n=input().lower()
p="aeiou"
co="qwrtypsdfghjklzxcvbnm"
l=0
k=len(n)-1
c=0
while l<k:
        if((n[l] in p and n[k] in co ) or (n[l]  in co and n[k] in p )):
            c+=1
        l+=1
        k-=1
print(c)
'''
here we cant keep not in p without taking co as they considered
space also as a character so cases or failed
if didnt understand ask me
'''
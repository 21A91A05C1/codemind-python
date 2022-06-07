n=input()
k="aeiou"
l=[]
s=[]
for i in n:
    if i  in k:
        l.append(i)
for i in k:
    if i not in l:
        s.append(i)
        
if(len(s)!=0):      
    print(*s)
    
else:
    print("0")
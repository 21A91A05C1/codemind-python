n=int(input())
k=(bin(n)[2:])
l=""
for i in k:
    if(i=='0'):
        l=l+'1'
    else:
        l=l+'0'
print(int(l,2))
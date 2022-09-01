n1=input().split(' ')
n=""
#print(n1)
for i in n1:
    n=n+i
#print(n)
print(min(n),n.count(min(n)),max(n),n.count(max(n)))
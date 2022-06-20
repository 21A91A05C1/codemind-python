s = input()
n = int(input())
res=0
n1=(n//len(s))
x=s.count('a')
x1=n1*x
x2=s[:n%(len(s))].count('a')
res=x1+x2
print(res)
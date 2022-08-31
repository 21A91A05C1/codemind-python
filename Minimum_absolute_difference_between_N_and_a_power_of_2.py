from math import log2,pow,floor
n=int(input())
left=pow(2,floor(log2(n)))
right=2*left
print(int(min((n-left),(right-n))))

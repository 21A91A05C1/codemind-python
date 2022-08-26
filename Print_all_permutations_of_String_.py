from itertools import permutations
s=input()
for i in permutations(s,len(s)):
    print("".join(i))
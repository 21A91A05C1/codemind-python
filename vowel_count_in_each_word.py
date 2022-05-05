n=input()
words=n.split()
for i in words:
    vowel=sum(letter in 'aeiou' for letter in i.lower())
    print(vowel,end=" ")
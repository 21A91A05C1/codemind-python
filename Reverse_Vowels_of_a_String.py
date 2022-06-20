def reverse_vowels(str1):
	v=""
	for char in str1:
		if char in "aeiouAEIOU":
			v+=char
	rs=""
	for i in str1:
		if i in "aeiouAEIOU":
			rs += v[-1]
			v=v[:-1]
		else:
			rs+= i
	return rs
str1=input()
print(reverse_vowels(str1))
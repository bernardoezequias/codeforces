def vasya_hello(s):
	word = 'hello'
	count = 0
	for i in range(len(s)):
		if s[i] == word[count]:
			count += 1
	
		if count == len(word):
			return 'YES'
	return 'NO'

s = input()
print(vasya_hello(s))

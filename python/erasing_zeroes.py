n = int(input())
removed_zeroes = []

for i in range(n):
	s = input()
	x = s.strip('0').count('0')
	removed_zeroes.append(x)

for num in removed_zeroes:
	print(num)



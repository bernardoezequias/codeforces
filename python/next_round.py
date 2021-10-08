n, k = map(int, input().split())
c = 0

entrada = input().split()

for i in range(len(entrada)):
	if int(entrada[i]) >= int(entrada[k-1]):
		if int(entrada[i]) >= 1:
			c += 1

print(c)


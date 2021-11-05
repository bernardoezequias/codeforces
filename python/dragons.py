s, n = map(int, input().split())
k_power = s
d_powerlist = []

for i in range(n):
	d_power, bonus = map(int, input().split())
	d_powerlist.append([d_power, bonus])

answer = 'NO'
d_powerlist.sort()

for i in range(n):
	if k_power > d_powerlist[i][0]:
		k_power += d_powerlist[i][1]
		answer = 'YES'
	else:
		answer = 'NO'
		break

print(answer)

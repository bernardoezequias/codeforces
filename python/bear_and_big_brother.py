lamak_weight, bob_weight = map(int, input().split())
years = 0

while bob_weight >= lamak_weight:
	years += 1
	bob_weight *= 2
	lamak_weight *= 3

print(years)

x = 0
n = int(input())
     
for i in range(n):
	op = input()

	if op[0:2] == "++" or op[1:3] == "++":
		x += 1
	elif op[0:2] == "--" or op[1:3] == "--":
		x -= 1

print(x)

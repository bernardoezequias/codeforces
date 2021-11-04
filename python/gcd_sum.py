n = int(input())

def gcd_sum(a, b):
        while True:
                for i in range(2, b+1):
                        if a % i == 0 and b % i == 0:
                                return a
                a += 1
                new_num = str(a)
                b = sum(map(int, new_num))

for i in range(n):
	num = input()
	a = int(num)	
	b = sum(map(int, num))
	
	print(gcd_sum(a,b))

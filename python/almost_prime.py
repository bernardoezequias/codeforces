def is_prime(num):
    divisors = 0
    for i in range(1, num):
        if num % i == 0:
            divisors += 1

    if divisors > 1 or num == 1:
        return False
    else:
        return True

n = int(input())
almost_primes = 0

for i in range(1, n+1):
    prime_divisors = 0
    for j in range(1, i):
        if i % j == 0 and is_prime(j):
            prime_divisors += 1

    if prime_divisors == 2:
        almost_primes += 1

print(almost_primes)


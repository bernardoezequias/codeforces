n = int(input())
numbers = list(map(int, input().split()))
even_sum = sum(numbers)
odd_numbers = []

for i in range(n):
    if numbers[i] % 2 != 0:
        odd_numbers.append(numbers[i])

numbers.sort()
odd_numbers.sort()

if even_sum % 2 == 0:
    print(even_sum)
else:
    even_sum -= odd_numbers[0]
    while even_sum % 2 != 0:
        if numbers[i] % 2 != 0:
            even_sum -= numbers[i]
            numbers.pop(i)

    print(even_sum)

n = int(input())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

for i in range(n - 1):
    if i % 2 == 0:
        numbers.pop(0)
    else:
        numbers.pop(-1)

print(numbers[0])

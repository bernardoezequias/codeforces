num_coins = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

taked_coins = list()

for i in range(num_coins):
    if sum(taked_coins[:i]) <= sum(coins[i:]):
        taked_coins.append(coins[i])

print(len(taked_coins))


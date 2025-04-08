def count_ways(n, coins, index):
    if n == 0:
        return 1
    if n < 0 or index == len(coins):
        return 0
    return count_ways(n - coins[index], coins, index) + count_ways(n, coins, index + 1)

coins = [500, 100, 10, 5, 1]

n = int(input("Enter the amount of money (n): "))

print("Number of ways to split the amount:", count_ways(n, coins, 0))
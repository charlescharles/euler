
coins = set([1, 2, 5, 10, 20, 50, 100, 200])

def ways(n):
    combinations = [0]*(n+1)
    combinations[0] = 1
    for c in coins:
        for j in range(c, n+1):
            combinations[j] += combinations[j-c]
    return combinations[n]

print ways(4)

from itertools import permutations
perms = permutations(range(10))

primes = [2, 3, 5, 7, 11, 13, 17]
def divisible(n):
    for i in range(1, 8):
        if int(n[i:i+3])%primes[i-1] != 0:
            return False
    return True
divisible(str(1406357289))

res = []
for p in perms:
    n = ''.join(map(str, p))
    if divisible(n):
        res.append(n)
print sum(res)
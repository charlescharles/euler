from itertools import permutations
perms = permutations(map(str, range(1, 10)))

def makes_product(p):
    for i in range(1, 6):
        for j in range(i+1, 8):
            if int(p[:i])*int(p[i:j]) == int(p[j:]):
                return p[j:]
    return None

res = []
for p in perms:
    n = ''.join(p)
    prod = makes_product(n)
    if prod:
        res.append((p, prod,))

products = set([pair[1] for pair in res])
print sum(map(int, list(products)))
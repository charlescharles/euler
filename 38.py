pandigits = list(range(1, 10))

def pandigital(n):
    return sorted(map(int, n)) == pandigits

def pseq(n):
    prods = []
    for i in range(1, 1000):
        prods.extend(list(str(i*n)))
        if len(set(prods)) < len(prods): return None
        if pandigital(prods): return ''.join(prods)
    return None
        

best = 0; best_i = 0
for i in range(90000):
    seq = pseq(i)
    if seq:
        best = max(best, int(seq))
        best_i = i
print best, best_i
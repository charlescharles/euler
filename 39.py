def right(p):
    solns = set()
    for a in range(1, p):
        for b in range(1, p-a):
            c = p - a - b
            if a**2 + b**2 == c**2:
                solns.add(tuple(sorted([a, b, c])))
    return len(solns)

best_p = 0; most = 0
for p in range(1, 1001):
    solns = right(p)
    if solns > most:
        most = solns
        best_p = p
print best_p, most
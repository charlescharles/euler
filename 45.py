def hex(c):
    "Returns True if c is hexagonal, else False"
    n = 0.25 * (1 + (1 + 8*c)**0.5)
    return int(n) == n

def pent(c):
    n = (1 + (1 + 24*c)**0.5)/6.0
    return int(n) == n

def triangle(n):
    "Return the nth triangle number"
    return (n*n + n)/2

for n in range(286, 100000):
    tr = triangle(n)
    if hex(tr) and pent(tr):
        print tr
        break
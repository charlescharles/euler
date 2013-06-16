def curious(a, b):
    num, den = map(lambda n: map(int, str(n)), [a, b])
    if num[0] in den and num[0] != 0:
        den.remove(num[0])
        num = num[1]
    elif num[1] in den and num[1] != 0:
        den.remove(num[1])
        num = num[0]
    else: return False
    den = den[0]
    if den == 0: return False
    if round(float(num)/den, 5) == round(float(a)/b, 5):
        return True
    return False

cur = []
for a in range(10, 100):
    for b in range(a+1, 100):
        if curious(a, b):
            cur.append((a, b,))

n, d = reduce(lambda p1, p2: (p1[0]*p2[0], p1[1]*p2[1],), cur)
for i in range(2, n):
    while n%i == d%i == 0:
        n /= i
        d /= i

print n, d
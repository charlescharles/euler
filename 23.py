limit = 28123

def dsum(n):
    "sum the divisors"
    ds = 0
    for i in range(1, n):
        if n%i == 0:
            ds += i
    return ds

def nexta(a):
    x = a+1
    while dsum(x) <= x:
        x += 1
    return x

candidate = [True for _ in range(limit)]
abundants = []; a = 11
while a <= limit:
    a = nexta(a)
    abundants.append(a)
    for b in abundants:
        if a+b < limit:
            candidate[a+b] = False

result = 0
for i in range(limit):
    if candidate[i]: result += i

print result
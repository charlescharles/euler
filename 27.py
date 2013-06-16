def prime(n):
    n = abs(n)
    for i in range(2, int(abs(n)**0.5)+1):
        if n%i == 0: return False
    return True

def degr(a, b):
    "return number of consec primes formed by"
    " n^2 + an + b"
    n = 0
    while prime(n**2 + a*n + b):
        n += 1
    return n

def expr(a, b):
    return n**2 + a*n + b

maxp = 0
for a in range(-999, 1000):
    for b in range(1000):
        if degr(a, b) > maxp:
            maxp = degr(a, b)
            j, k = a, b

print maxp
print j, k


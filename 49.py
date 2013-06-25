import pyprimes as pp
import itertools as it

four_primes = []
for p in pp.primes_above(1000):
    if p >= 9999: break
    four_primes.append(p)
N = len(four_primes)

def prime_perms():
    for i in range(N):
        for j in range(i+1, N):
            a, b = four_primes[i], four_primes[j]
            c = 2*b - a
            if set(str(a)) == set(str(b)) == set(str(c)) and pp.isprime(c):
                print a, b, c

prime_perms()
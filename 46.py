N = int(1e4)
prime = [True]*N
prime[0] = prime[1] = False
for i in range(2, N):
    if prime[i]:
        for j in map(lambda x: i*x, range(2, N/i+1)):
            if j < N:
                prime[j] = False

primes = []
composites = []
for i in range(2, N):
    if prime[i]: primes.append(i)
    else: composites.append(i)

odd_composites = [x for x in composites if x&1]

for x in odd_composites:
    found = False
    for p in primes:
        if p > x: break
        n = ((x-p)/float(2))**0.5
        if int(n) == n:
            found = True
            break
    if not found:
        print x
        break
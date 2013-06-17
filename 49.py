N = int(1e4)
prime = [True]*N
prime[0] = prime[1] = False
for i in range(2, N):
    if prime[i]:
        for j in map(lambda x: i*x, range(2, N/i+1)):
            if j < N:
                prime[j] = False
four_primes = []
for i in range(1000, N):
    if prime[i]: four_primes.append(i)

print four_primes[:100]
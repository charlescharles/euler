N = int(1e6)
prime = [True]*N
prime[0] = prime[1] = False
for i in range(2, N):
    if prime[i]:
        for j in map(lambda x: i*x, range(2, N/i+1)):
            if j < N:
                prime[j] = False
primes = []
for i in range(2, N):
    if prime[i]: primes.append(i)

best = 539
win = 0
num_primes = len(primes)
for k in range(best, 547):
    for i in range(k, num_primes):
        s = sum(primes[i-k:i])
        if s < N and prime[s]:
            best = k; win = s
            print best, win
            break
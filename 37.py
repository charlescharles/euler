N = int(1e6)

prime = [True]*N
prime[0] = prime[1] = False
for i in range(N):
    if prime[i]:
        for j in map(lambda x: x*i, range(2, (N/i)+1)):
            if j < N:
                prime[j] = False

def truncatable(p):
    p = str(p)
    for k in range(1, len(p)):
        if not (prime[int(p[:k])] and prime[int(p[-k:])]):
            return False
    return True

tprimes = []
for i in range(10, N):
    if prime[i] and truncatable(i):
        tprimes.append(i)

print tprimes
print len(tprimes)
print sum(tprimes)
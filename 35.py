def rotations(n):
    n = list(str(n))
    res = []
    for _ in range(len(n)):
        n.append(n.pop(0))
        res.append(n[:])
    return map(lambda l: int(''.join(l)), res)


N = int(1e6)
prime = [True for _ in range(N)]
prime[0] = prime[1] = False
for i in range(2, N):
    if prime[i]:
        for j in map(lambda x: i*x, range(2, N/i+1)):
            if j < N:
                prime[j] = False

def circular(n):
    for x in rotations(n):
        if not prime[x]: return False
    return True

ct = 0
for i in range(2, N):
    if circular(i):
        ct += 1

print ct
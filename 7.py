N = int(1e6)

p = [True for _ in range(N)]
p[0] = p[1] = False

for i in range(2, N):
	if p[i]:
		for j in map(lambda x: i*x, range(2, N/i+1)):
			if j < N: p[j] = False

primes = []
count = 0
for i in range(2, N):
	if p[i]:
		primes.append(i)
		count += 1
		if count == 10001:
			print i


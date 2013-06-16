
def d(n):
	dsum = 1
	for i in range(2, n):
		if n%i == 0:
			dsum += i
	return dsum

N = 10000
seen = [False for _ in range(N)]
amicable = [False for _ in range(N)]
for n in range(N):
	if not seen[n]:
		dn = d(n)
		if d(dn) == n and dn < N and n != dn:
			amicable[n] = amicable[dn] = True
		seen[n] = True
		if dn < N: seen[dn] = True

asum = 0
#amicables = []
for n in range(N):
	if amicable[n]:
		asum += n
		#amicables.append(n)

print asum
import time

def T(n):
	return n*(n+1)/2

def makeprimes(N):
	p = [True for _ in range(N)]
	p[0] = p[1] = False
	for i in range(N):
		if p[i]:
			for j in map(lambda x: i*x, range(2, N/i+1)):
				if j < N:
					p[j] = False
	primes = set()
	for i in range(N):
		if p[i]:
			primes.add(i)
	return primes

def maket(N):
	for i in range(1, N):
		yield T(i)

start = time.clock()
primes = makeprimes(int(1e6))
end = time.clock()

print 'time taken: ', end-start

def divisors(n):
	d = {}
	for p in primes:
		if n%p == 0:
			count = 0
			while n%p == 0:
				n /= p
				count += 1
			d[p] = count
	return d

def nfactors(n):
	nf = 1
	for k, v in divisors(n).items():
		nf *= v+1
	return nf

for i, n in enumerate(maket(int(1e6))):
	nf = nfactors(n)
	if nf > 500:
		print 'the {}th triangular number, {}, has {} factors'.format(i, n, nf)
		break
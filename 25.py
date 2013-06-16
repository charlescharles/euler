f = {}
def fib(n):
	if n == 1 or n == 2: return 1
	if n in f:
		return f[n]
	fn = fib(n-1) + fib(n-2)
	f[n] = fn
	return fn

def dcount(n):
	return len(str(n))

digits = 1000
for n in range(1, 20000):
	fn = fib(n)
	if dcount(fn) == digits:
		print n, fn
		break

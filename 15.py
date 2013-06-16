def rfac(a, b):
	return reduce(lambda x, y: x*y, range(a, b+1))

def paths(n):
	return rfac(n+1, 2*n)/rfac(1, n)

print paths(20)
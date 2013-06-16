digits = 10
def npn(n):
	"Return last 10 digits of n^n"
	prod = 1
	for _ in range(n):
		prod *= n
		strprod = str(prod)
		if len(strprod) > digits:
			prod = int(strprod[-digits:])
	return prod

def add(x, y):
	s = x + y
	strs = str(s)
	if len(strs) > digits:
		s = int(strs[-digits:])
	return s

def nrange(n):
	for x in range(1, n+1):
		yield npn(x)

last = 0
for x in nrange(1000):
	last = add(last, x)
print last
power = 1000
N = 1 << power

dsum = 0
for x in map(int, str(N)):
	dsum += x

print dsum
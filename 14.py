collatz = {1:1, 2:2}
def clength(n):
	if n in collatz: return collatz[n]
	clen = 0; x = n
	while x not in collatz:
		if x&1: x = 3*x + 1
		else: x = x >> 1
		clen += 1
	clen += collatz[x]
	collatz[n] = clen
	return clen

win = 1
maxclen = 0
for x in range(1, int(1e6)):
	clen = clength(x)
	#print x, clen
	if clen > maxclen:
		maxclen = clen
		win = x
print win, maxclen

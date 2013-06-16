factorial = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720}
for x in range(7, 10):
	factorial[x] = x*factorial[x-1]

curious = []
csum = 0
for x in range(10, int(41000)):
	if x == sum(map(lambda x: factorial[int(x)], str(x))):
		curious.append(x)
		csum += x
print csum
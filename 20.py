n = 100

prod = 1
for i in range(1, n+1):
	prod *= i
	while prod%10 == 0:
		prod /= 10

print sum(map(int, list(str(prod))))
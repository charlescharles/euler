def isDivisible(n):
	for i in range(1,21):
		if n%i != 0: return 0
	return 1

if __name__ == "__main__":
	n = 0
	while n < 10**10:
		if isDivisible(2520+n): break
		n += 1
	print(2520+n)
	
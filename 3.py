def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n%i == 0: return 0
	return 1

def largestPrimeFactor(n):
	for i in range(1, n):
		if n%i==0 and isPrime(n/i): return (n/i)

if __name__ == "__main__":
	print(largestPrimeFactor(600851475143))
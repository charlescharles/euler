def isEven(n):
	num = list(str(n))
	last = int(num[len(num)-1])
	if last%2 == 0: return 1
	return 0

def fib(n1, n2, max, sum):
	print(n2)
	if n2 < max and isEven(n2): sum += n2
	if n2 > max: return sum
	return fib(n2, n1+n2, max, sum)

if __name__ == "__main__":
	print("sum is " + str(fib(0, 1, 4*10**6, 0)))

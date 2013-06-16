def isEven(n):
	num = list(str(n))
	last = int(num[len(num)-1])
	if last%2 == 0: return 1
	return 0

if __name__ == "__main__":
	i = 0
	j = 1
	k = 1
	sum = 0
	while j < (4*10**6):
		print(repr((j,k)))
		i = k
		k = j + k
		j = i
		if isEven(k): sum += k
	print(sum)
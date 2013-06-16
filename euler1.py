def isMult5(n):
	num = list(str(n))
	length = len(num)
	if num[length-1]=='0' or num[length-1]=='5':
		return 1

def isMult3(n):
	num = list(str(n))
	length = len(num)
	if length==1:
		if n==3 or n==6 or n==9:
			return 1
		return 0

	sum = 0
	for i in range(length):
		sum += int(num[i])
	return isMult3(sum)

if __name__ == "__main__":
	nsum = 0
	for i in range(1000):
		if isMult3(i) or isMult5(i): nsum += i
	print(nsum)
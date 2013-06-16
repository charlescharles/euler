def isPalindrome(n):
	num = list(str(n))
	half = len(num)//2
	for i in range(half):
		if num[i]!=num[len(num)-1-i]: return 0
	return 1

def findPalindrome(length):
	rg = 10**(length) - 10**(length-1)
	maxnum = 10**(length) - 1
	largestp = 0
	for i in range(rg):
		for j in range(rg):
			if isPalindrome((maxnum-i)*(maxnum-j)) and ((maxnum-i)*(maxnum-j))>largestp: largestp=((maxnum-i)*(maxnum-j))
	return largestp
	
if __name__ == "__main__":
	print(findPalindrome(3))
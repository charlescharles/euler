def palindrome(s):
	n = len(s)
	if n == 1: return True
	return s[:n/2] == s[-(n/2):][::-1]

def binar(x):
	return '{0:b}'.format(x)

nsum = 0
res = []
for x in range(int(1e6)):
	if palindrome(str(x)) and palindrome(binar(x)):
		nsum += x
		res.append(x)

print nsum

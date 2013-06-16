words = {
	0:'',
	1:'one',
	2:'two',
	3:'three',
	4:'four',
	5:'five',
	6:'six',
	7:'seven',
	8:'eight',
	9:'nine',
	10:'ten',
	11:'eleven',
	12:'twelve',
	13:'thirteen',
	14:'fourteen',
	15:'fifteen',
	16:'sixteen',
	17:'seventeen',
	18:'eighteen',
	19:'nineteen',
	20:'twenty',
	30:'thirty',
	40:'forty',
	50:'fifty',
	60:'sixty',
	70:'seventy',
	80:'eighty',
	90:'ninety',
	100:'hundred',
}

def towords(n):
	if n <= 20:
		return words[n]
	if n < 100:
		t = (n//10)
		return words[t*10] + words[n-10*t]
	if n < 1000:
		h = (n//100)
		if n == 100*h:
			return words[h] + 'hundred'
		if n - 100*h <= 20:
			return words[h] + 'hundredand' + words[n-100*h]
		t = (n - 100*h)//10
		return words[h] + 'hundredand' + words[t*10] + words[n-100*h-10*t]
	return 'onethousand'

lens = {}
for n, leng in words.items():
	lens[n] = len(leng)


def wordlen(n):
	if n <= 20:
		return lens[n]
	if n < 100:
		t = n//10
		return lens[10*t] + lens[n-10*t]
	if n < 1000:
		h = n//100
		if n == 100*h:
			return lens[h] + 7
		if n - 100*h <= 20:
			return lens[h] + 10 + lens[n-100*h]
		t = (n-100*h)//10
		return lens[h] + 10 + lens[10*t] + lens[n-100*h-10*t]
	return 11

n=300
print towords(n), len(towords(n)), wordlen(n)

total = 0
for n in range(1, 1001):
	total += wordlen(n)

print total

with open('names.txt', 'r') as f:
	data = map(lambda name: name[1:-1], f.read().split(','))

data.sort()
a = ord('A')

def value(name):
	val = 0
	for c in name:
		val += ord(c) - a + 1
	return val

score = 0
for i, name in enumerate(data):
	score += (i+1)*value(name)
print score
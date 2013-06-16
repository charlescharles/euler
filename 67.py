data = []
with open('triangle.txt', 'r') as f:
	for line in f:
		data.append(map(int, line.split()))

def maxsum(data):
	curr = data[-1][:]
	for i in range(len(data)-2, -1, -1):
		curr = [max(curr[j], curr[j+1]) + data[i][j] for j in range(len(data[i]))]
	return curr[0]

print maxsum(data)
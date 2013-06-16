def sumto(N):
	s = 0
	for i in range(1 , (N-1)/2 + 1):
		s += 4*i**2 + 4*i + 1
		s += 4*i**2 + 1
		s += 4*(i+1)**2 - 10*(i+1) + 7
		s += 4*(i+1)**2 - 6*(i+1) + 3
	return 1+s

print sumto(1001)
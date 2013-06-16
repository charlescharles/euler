N = int(2e6)

remains = [True for _ in range(N)]
remains[0] = remains[1] = False
for i in range(2, N):
    if remains[i]:
        for j in map(lambda x: i*x, range(2, N//i+1)):
            if j < N:
                remains[j] = False

primesum = 0
for i in range(2, N):
    if remains[i]:
        print i
        primesum += i

print 
print primesum
def nfactors(n):
    i = 2; ct = 0
    while n > 1:
        if n % i == 0:
            ct += 1
            while n % i == 0:
                n /= i
        i += 1
    return ct

for i in range(10, int(1e6)):
    if nfactors(i)==4 and nfactors(i-1)==4 and nfactors(i-2)==4 and nfactors(i-3)==4:
        print i-3
        break
        
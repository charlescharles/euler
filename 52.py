from collections import Counter

for k in range(1, int(1e6)):
    mults = map(lambda n: Counter(map(int, str(n))), [k*i for i in range(1, 7)])
    if mults.count(mults[0]) == len(mults):
        print k
        break
import math

def combos(amax, bmax):
    c = set()
    for i in range(2, amax+1):
        for j in range(2, bmax+1):
            c.add(int(math.pow(i, j)))
    return len(c)

print combos(100, 100)

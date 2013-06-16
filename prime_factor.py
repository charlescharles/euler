def isprime(n):
    if n < 2: return False
    if n == 2: return True
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n%x == 0:
            return False
    return True

def lpf(n):
    for x in xrange(3, n, 2):
        if n%x == 0 and isprime(n/x):
            return n/x
    return -1


if __name__ == '__main__':
    print(lpf(600851475143))
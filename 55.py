N = 5000

def palindrome(n):
    n = str(n); m = len(n)
    return n[:m/2] == n[-(m/2):][::-1]

def iter(n):
    return n + int(str(n)[::-1])

def lychrel(n):
    for k in range(49):
        n = iter(n)
        if palindrome(n): return False
    return True

count = 0
for i in range(1, 10000):
    if lychrel(i): count += 1
print count


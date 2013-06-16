def reverse(a, start, end):
    "reverse a from start to end inclusive"
    return a[:start] + a[start:end+1][::-1] + a[end+1:]

def nextlex(n):
    k = 8; l = 9
    while n[k] > n[k+1]: k -= 1
    while n[l] < n[k]: l -= 1
    n[k], n[l] = n[l], n[k]
    n = reverse(n, k+1, 9)
    return n

n = map(int, list('0123456789'))

for i in range(int(1e6)-1):
    n = nextlex(n)

print ''.join(map(str, n))
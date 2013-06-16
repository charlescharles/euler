def strlen(n):
    "Return the number of digits in decimal representation"
    return len(str(n))

def nth(n):
    pos = cur = 1
    while pos+strlen(cur) <= n:
        pos += strlen(cur)
        cur += 1
    for c in str(cur):
        if pos == n: return int(c)
        pos += 1
    return None

prod = 1
for k in [1, 10, 100, 1000, int(1e4), int(1e5), int(1e6)]:
    prod *= nth(k)
print prod
triangles = set()
for n in range(1, 101):
    triangles.add((n*n+n)/2)

with open('words.txt', 'r') as f:
    words = map(lambda s: s.lower(), f.read().split("\",\""))

print words[:10]

a = ord('a')
def wordsum(w):
    s = 0
    for c in w:
        s += ord(c) - a + 1
    return s

def triangle_word(w):
    ws = wordsum(w)
    if ws > 5050:
        print 'wordsum of {} is >5050'.format(w)
    return wordsum(w) in triangles

print triangle_word('sky')

ct = 0
for w in words:
    if triangle_word(w):
        ct += 1
print ct
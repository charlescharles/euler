def pandigital(n):
    return len(set(n)) == len(n)

def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def next_lex(a):
    k = len(a) - 2; l = k + 1
    while a[k] > a[k+1]: k -= 1
    if k < 0: return None
    while a[k] > a[l]: l -= 1
    a[k], a[l] = a[l], a[k]
    return reverse(a, k+1, len(a)-1)

from math import ceil
def reverse(a, start, end):
    for i in range(int(ceil((end-start)/2.0))):
        a[start+i], a[end-i] = a[end-i], a[start+i]
    return a

def largest_pandigital(n):
    print 'examining {}-pandigital numbers'.format(n)
    digits = list(range(n, 0, -1))
    inorder = list(range(1, n))
    i = 0
    while True:
        i += 1
        if i%10000 == 0: print 'examined ', i
        if (digits[-1] != 2 and digits[-1] != 0) and prime(int(''.join(map(str, digits)))):
            print ''.join(map(str, digits))
            return
        digits = [-1*x for x in next_lex([-1*y for y in digits])]
        #print 'looking at ', ''.join(map(str, digits))


largest_pandigital(7)
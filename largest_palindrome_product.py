def ispalindrome(x):
    for i in xrange(len(x)/2):
        if x[i] != x[-(1+i)]:
            return False
    return True


def largest_palindrome():
    largest = 0
    for i in xrange(999,500,-1):
        for j in xrange(999,500,-1):
            if ispalindrome(str(i*j)):
                largest = max(largest, i*j)
    return largest

if __name__ == '__main__':
    print(largest_palindrome())
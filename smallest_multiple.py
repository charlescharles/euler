def smallest_multiple(n):
    left = [i for i in range(2, n+1)]
    for x in range(n-1):
        for y in range(x+1, n-1):
            if left[y]%left[x] == 0:
                left[y] /= left[x]
    return left

print reduce(lambda x,y: x*y, smallest_multiple(20))
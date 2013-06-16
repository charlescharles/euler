def greatest_product(n):
    times = lambda x,y: x*y
    prod = reduce(times, map(int, n[:5]))
    maxprod = prod
    


subnums = num.split('0')
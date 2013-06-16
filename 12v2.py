def d(num):
    factors = []
    processed = []
    div = 2
    while num > 1:
        while num % div == 0:
            factors.append(div)
            num /= div
        div += 1

    X = 1
            
    for prime in factors:
        if processed.count(prime) > 0:
            continue
        else:
            processed.append(prime)
            X *= (factors.count(prime) + 1)
    return X

for i in range(1, 10000001):
    Triangle = int((i*(i + 1))/2)
    divisors = d(Triangle)
    if divisors > 500:
        print(Triangle, "is the answer!")
        break
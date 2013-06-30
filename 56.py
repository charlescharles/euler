def digit_sum(a, b):
    return sum([int(x) for x in str(a**b)])

most = 0
for i in range(2, 100):
    for j in range(2, 100):
        most = max(most, digit_sum(i, j))

print most
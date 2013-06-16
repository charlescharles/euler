limit = int(2e6)
p = 5

res = 0
nums = []
for n in range(10, limit):
    if n == sum(map(lambda d: pow(int(d), p), list(str(n)))):
        res += n
        nums.append(n)

print res
print nums
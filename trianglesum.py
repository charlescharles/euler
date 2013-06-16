import itertools
import operator
import time

def timeit(fn):
	def timer():
		start = time.clock()
		for d in data:
			fn(d)
		end = time.clock()
		print fn.__name__ + ' took {} seconds'.format(end-start)
	return timer


data = [[
        [1],
        [2, 3],
        [3, 3, 1],
        [3, 1, 5, 4],
        [3, 1, 3, 1, 3],
        [2, 2, 2, 2, 2, 2],
        [5, 6, 4, 5, 6, 4, 3]
    ],
    [
        [1],
        [2, 1],
        [1, 2, 1],
        [1, 2, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 2, 1, 1, 1, 1],
        [1, 2, 1, 1, 1, 1, 9]
    ],
    [
        [9],
        [2, 2],
        [3, 3, 3],
        [4, 4, 4, 4]]] 


@timeit
def checkio1(data):
    """
    Return the maximum possible sum in a path from the top to bottom.
    data: A list of lists of integers, representing the weights per cell.
    """
    current = []
    for row in data:
        extended = map(max, zip([0] + current, current + [0]))
        #current = list(itertools.starmap(operator.add, zip(extended, row)))
        current = list(map(sum, zip(extended, row)))
    return max(current)

checkio1()

'''
@timeit
def checkio2(d):
	return d[0][0] if len(d) < 2 else checkio2(d[:-2] + [[max(a, b) + c for a, b, c in zip(d[-1], d[-1][1:], d[-2])]])

checkio2()'''

@timeit
def checkio3(data):
    """list[list[int]] -> int
    Return max possible sum in a path from top to bottom
    """
 
    best = data[0]
    for row in data[1:]:
        best = [max(a, b) for a, b in \
            zip([a + b for a, b in zip(best + [0], row)], \
                [a + b for a, b in zip([0] + best, row)])]
         
    return max(best)


checkio3()

@timeit
def checkio4(data):
    """list[list[int]] -> int
    Return max possible sum in a path from top to bottom
    """
    if not data:
        return 0
    accum = data[-1][:]
    for i in range(len(data) - 2, -1, -1):
        accum = [max(accum[j], accum[j + 1]) + data[i][j]
                 for j in range(len(data[i]))]
    return accum[0]


checkio4()
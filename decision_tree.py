import re
from collections import OrderedDict

def prob(features, tree, init=1.0):
	init *= tree[0]
	if len(tree) == 1: return init
	if tree[1] in features:
		return prob(features, tree[2], init)
	return prob(features, tree[3], init)

def parse_tree(lines):
	expr = ' '.join(lines)
	expr = expr.replace('(', '[')
	expr = expr.replace(')', ']')
	expr = re.sub(r"([0-9a-z]) \[", r"\1, [", expr)
	expr = re.sub(r"\] \[", r"], [", expr)
	expr = re.sub(r"([0-9]) ([a-z])", r"\1, \2", expr)
	expr = re.sub(r"([a-z]+)", r"'\1'", expr)
	return eval(expr)


def read_tree(f):
	n_lines = int(f.readline())
	lines = []
	for x in range(n_lines):
		lines.append(f.readline().strip())
	return parse_tree(lines)

def read_animals(f):
	n_animals = int(f.readline())
	animals = OrderedDict()
	for x in range(n_animals):
		line = f.readline().strip().split()
		if len(line) > 2:
			animals[line[0]] = line[2:]
		else:
			animals[line[0]] = []
	return animals

def solve_one(f, f_out):
	tree = read_tree(f)
	features = read_animals(f)
	for an in features:
		f_out.write("%.6f\n" % prob(features[an], tree))

f = open('in', 'r')
f_out = open('out', 'w')
for k in range(int(f.readline())):
	f_out.write("Case #{}:\n".format(k+1))
	solve_one(f, f_out)
f.close()
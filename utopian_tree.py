def utopian_tree(p):
	h = 1
	for i in range(1,p+1):
		if i % 2 != 0:
			h *= 2
		else:
			h += 1
	return h
print(utopian_tree(5))
import math
s = list(input().strip)
L = len(s)
row = math.floor(math.sqrt(L))
col = math.ceil(math.sqrt(L))

for i in range(col):
	x = 0
	while True:
		try:
			print(s[i+x], end ='')
			x += col 
		except:
			break
	print(' ', end = '')
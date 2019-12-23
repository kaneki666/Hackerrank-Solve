def beautifulDays(i, j, k):
	day = 0
	for i in range(i,j+1):
		x = str(i)
		rev_x = x[::-1]
		x_int = int(x)
		print(x_int)
		rev_x_int = int(rev_x)
		if (x_int-rev_x_int) % k == 0:
			day += 1
		else:
			print("not beautifulDays")
	return day

print(beautifulDays(20,23,6))
digit = 1104444
digits = [int(x) for x in str(digit)]
count = 0
for i in digits:
	if i !=0 and (digit % i) == 0 :
		count += 1

print(count)
	


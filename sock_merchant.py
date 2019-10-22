n = 3
arr = [1,2,3,1,2,3]
pair = 0
d = {}
for i in arr:
	if arr[i] in d:
		d.pop(arr[i])
		pair += 1
	else:
		d[arr[i]] = 1
print(pair)


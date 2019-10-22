arr = [1,2,3,4,5,6]
k = 5
count = 0
for i in range(len(arr)-1):
	for j in range(i+1,len(arr)):
		if (arr[i] + arr[j]) % k == 0:
			count += 1
print(count)

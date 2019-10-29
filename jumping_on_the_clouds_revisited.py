def couldjump(arr,j):
	score = 100
	for i in range(0,len(arr),j):
		print(arr[i])
		if arr[i] == 1:
			score =  score-1-2
		else:
			score =score -1			
	return score
print(couldjump([0, 0, 1, 0, 0, 1, 1, 0],2))

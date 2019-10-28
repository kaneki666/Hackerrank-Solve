import math
def strange_advertising(n):	
	liked = 0
	given_value = 5
	for i in range(n):
		liked += math.floor(given_value/2)
		given_value = math.floor(given_value/2)*3
	return liked
print(strange_advertising(3))
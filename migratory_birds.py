count = [0]*6
arr = [1,2,3,3,4]
for t in arr:
    count[t] += 1
maxVal = max(count)
ans = count.index(maxVal)
print(ans)
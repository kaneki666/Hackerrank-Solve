
def cutTheSticks(arr):
    arr = list(sorted(arr))
    result = []
    while len(arr) != 0:
        result.append(len(arr))
        min_val = min(arr)
        while True:
            try:
                arr.remove(min_val)
            except ValueError:
                break
    return result	
print(cutTheSticks([5, 4, 4, 2, 2, 8]))

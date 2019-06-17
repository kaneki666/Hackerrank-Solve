import math

def insertion_sort(collection):
    for index in range(1, len(collection)):
        while 0 < index and collection[index] < collection[index - 1]:
            collection[index], collection[
                index - 1] = collection[index - 1], collection[index]
            index -= 1

    return collection

def bucket_sort(arr):
    N = len(arr)
    Max = max(arr)
    Min = min(arr)
    bucket_size = 10
    bucket_count = math.floor((Max + 1) / bucket_size)
    bucket = []
    for i in range(0,bucket_count):
        bucket.append([])
    for i in range(0,N):
        bucket[math.floor(bucket_count / bucket_size)].append(arr[i])
    sortedArray = []
    for i in range(0, len(bucket)):
        insertion_sort(bucket[i])
        for j in range(0, len(bucket[i])):
            sortedArray.append(bucket[i][j])

    return sortedArray
arr = [12, 23, 4, 5, 3, 2, 12, 81, 56, 95]
print("Unsorted array is-",arr)
print("Sorted array is-",bucket_sort(arr))



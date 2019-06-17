data = [1,3,5,7,8,9,12,14,15,18,16,21,24,25,29,30]
target = 12

def binary_search_iterative(data , target):
    min = 0
    max = len(data) - 1
    while min <= max:
        mid = (min + max) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            max = mid - 1
        else:
            min = mid + 1
    return False


def binary_search_recursive(data , target , min , max):
    if min > max:
        return False
    else:
        mid = (min + max) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data , target , min , mid - 1)
        else:
            return binary_search_recursive(data , target , mid + 1 , max)

print(binary_search_iterative(data, target))
print(binary_search_recursive(data , target , 0 , len(data)-1))
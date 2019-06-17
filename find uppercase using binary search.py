input_string_1 = "saDman"
input_string_2 = "SadMan"
input_string_3 = "sadman"

def binary_search_iterative(input_string):
    for i in range(len(input_string)):
        if input_string[i].isupper():
            return input_string[i]
    return "No uppercase charchter is found"

def binary_search_recursive(input_string , index = 0 ):
    if input_string[index].isupper():
        return input_string[index]
    if index == len(input_string) - 1:
        return "No uppercase charchter is found"
    return binary_search_recursive(input_string , index + 1)

print(binary_search_iterative(input_string_1))
print(binary_search_iterative(input_string_2))
print(binary_search_iterative(input_string_3))
print(binary_search_recursive(input_string_1))
print(binary_search_recursive(input_string_2))
print(binary_search_recursive(input_string_3))
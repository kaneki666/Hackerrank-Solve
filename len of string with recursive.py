input_str = "algorithm"

def iterative_len(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

def recursive_len(input_str):
    if input_str == "":
        return 0
    return 1 + recursive_len(input_str[1:])

print(iterative_len(input_str))
print(recursive_len(input_str))


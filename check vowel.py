input_str1 = "learn programming"
input_str2 = "algorithm"
vowel = "aeiou"

def iterative(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha():
            count += 1
    return count


def recursive(input_str):
    if input_str == "":
        return 0
    if input_str[0].lower() not in vowel and input_str[0].isalpha():
        return 1 + recursive(input_str[1:])
    else:
        return recursive(input_str[1:])

print(iterative(input_str1))
print(recursive(input_str1))
print(iterative(input_str2))
print(recursive(input_str2))
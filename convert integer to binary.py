from stack import Stack

def div_fun(decimal_val):
    s = Stack()
    while decimal_val > 0:
        remainder = decimal_val % 2
        s.push(remainder)
        decimal_val = decimal_val // 2
    
    binary_val = " "
    while not s.is_empty():
        binary_val += str(s.pop())
    return binary_val

print(div_fun(4510))

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items

def reverse_string(stack , input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_string = " "
    while not stack.is_empty():
        rev_string += stack.pop()
    return rev_string

stack = Stack()
input_str = (" settenoiram ekil ecnad eW steerts eht hguorht star deL repiP deiP eht ekil tsuJ")
x=reverse_string(stack, input_str)
print(x)

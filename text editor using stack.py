from stack import Stack
Q=int(input().strip())
string = Stack()
for _ in range(Q):
    x= input().split()
    if x[0] == '1':
        string.name = string.push(x[1])
    elif x[0] == '2':
        string.delete(int(x[1]))
    elif x[0] == '3':
        print(string.name[int(x[1])-1])
    elif x[0] == '4':
        string.undo()

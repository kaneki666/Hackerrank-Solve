def staircase(a):
    for i in range(1, a + 1):
        print((a - i) * ' ' + i * "#")
print(staircase(5))

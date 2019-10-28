i = [20,21,22,23]
k = 6
count = 0
for x in i:
    if (x - int(str(x)[::-1])) % k == 0:
        count += 1
print(count)
k = 3
a = [-1, -3, 4, 2]
count = 0
for i in a:
    if i < 1:
        count += 1
print(count)    
if (count) >= k:
    print('YES')
else:
    print('NO')
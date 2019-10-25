from string import ascii_lowercase
word = "name"
result = []
a = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
for i in word:
	result.append(a[ascii_lowercase.index(i)])
print(result)
h = max(result)
print(h)
pdf = h* len(word)
print(pdf)



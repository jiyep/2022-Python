a = ['a', 'b', 'c', 'd', 'e']
b = [1, 2, 3]

for s in zip(a, b):
    print(s)
    print(list(s))

print("=========================")

x = ['a', 'b', 'c']
y = [1, 2, 3]
z = []

for x, y in zip(x, y):
    z.append(x)
    z.append(y)
print(z)

print("=========================")

dictionary = dict.fromkeys(z, 0)
print(dictionary)
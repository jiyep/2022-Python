a = {'a': 100, 'b': 50, 'm': 60}
print(a)

a['grape'] = 150
print(a)

a['b'] = 300
print(a)

del a['b']
print(a)

for k in a.keys():
    print("key = ", k)

print()

for v in a.values():
    print("values = ", v)

print()

for k, v in a.items():
    print("key = ", k, "values = ", v)
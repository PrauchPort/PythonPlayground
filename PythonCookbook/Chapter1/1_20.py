from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}


c = ChainMap(a, b)

for item in c.items():
    print(item)

c['x'] = 11
c['z'] = 12

for item in c.items():
    print(item)

print(a)
print(b)

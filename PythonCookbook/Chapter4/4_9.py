from itertools import permutations, combinations, combinations_with_replacement
items = ['a', 'b', 'c']

for p in permutations(items):
    print(p)

print('-'*20)

for p in permutations(items, r=2):
    print(p)

print('-'*20)

for c in combinations(items, r=3):
    print(c)

print('-'*20)

for c in combinations(items, r=2):
    print(c)


print('-'*20)

for c in combinations(items, r=1):
    print(c)


print('-'*20)

for c in combinations_with_replacement(items, r=3):
    print(c)


print('-'*20)

for c in combinations_with_replacement(items, r=1):
    print(c)

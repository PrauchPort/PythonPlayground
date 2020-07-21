def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


l = [1, 5, 1, 2, 6, 4, 2, 1, 6, 78, 3, 2, 4,
     7, 8, 54, 4, 76, 4, 6, 4, 6, 7, 4, 22, 4]

a = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}, {'x': 3, 'y': 4}]

print(list(dedupe(l)))

print(list(dedupe(a, key=lambda x: (x['x'], x['y']))))

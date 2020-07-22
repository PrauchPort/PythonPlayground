from operator import itemgetter

d = [
    {'name': 'Jan', 'surname': 'Kowalsk', 'age': 20},
    {'name': 'Andrzej', 'surname': 'Kowalsk', 'age': 18},
    {'name': 'Michal', 'surname': 'Kowalsk', 'age': 30},
    {'name': 'Tomasz', 'surname': 'Kowalsk', 'age': 7},
]

rows_by_name = sorted(d, key=itemgetter('name'))
rows_by_age = sorted(d, key=itemgetter('age'))

print(rows_by_name)
print(rows_by_age)

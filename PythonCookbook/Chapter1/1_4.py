import heapq


if __name__ == '__main__':

    l = [6, 23, 7, 2, 123, 31, 12, 3, 532, 5, 211, 2, 49, 94, 83]

    print(heapq.nlargest(5, l))
    print(heapq.nsmallest(3, l))

    d = [
        {'name': 'Jan', 'surname': 'Kowalsk', 'age': 20},
        {'name': 'Andrzej', 'surname': 'Kowalsk', 'age': 18},
        {'name': 'Michal', 'surname': 'Kowalsk', 'age': 30},
        {'name': 'Tomasz', 'surname': 'Kowalsk', 'age': 7},
    ]

    print(heapq.nlargest(5, d, key=lambda x: x['age']))
    print(heapq.nsmallest(3, d, key=lambda x: x['name']))

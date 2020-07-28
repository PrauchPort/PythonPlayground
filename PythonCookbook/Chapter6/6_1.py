import csv
from collections import namedtuple

with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for row in f_csv:
        row = Row(*row)
        print(row)

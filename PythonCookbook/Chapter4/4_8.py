from itertools import dropwhile

with open('file.txt') as f:
    for line in dropwhile(lambda line: 'python' in line, f):
        print(line)

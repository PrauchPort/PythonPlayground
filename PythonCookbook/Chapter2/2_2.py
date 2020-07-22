from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))

print(fnmatch('foo.txt', '$.txt'))

print(fnmatch('foo27.txt', '*[1-6]*.txt'))


print(fnmatchcase('foo27.txt', '*[1-6]*.TXT'))
print(fnmatchcase('foo27.txt', '*[1-6]*.txt'))

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

print('-'*20)

d1 = dict()
d1['foo'] = 1
d1['bar'] = 2
d1['spam'] = 3
d1['grok'] = 4

for key in d1:
    print(key, d1[key])

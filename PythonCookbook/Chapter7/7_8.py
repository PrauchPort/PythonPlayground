from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


spam('sad', 'asd', 'dsa', 'aaa')

s1 = partial(spam, 'aaa', 'ssss')

s1('asdad', 'qwe')


s2 = partial(spam, b='2', d='4')

s2('1', c='3')

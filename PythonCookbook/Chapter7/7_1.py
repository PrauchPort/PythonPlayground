def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2))


def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


print(anyargs(1, 2, 1, 2, name='777', surname='444'))

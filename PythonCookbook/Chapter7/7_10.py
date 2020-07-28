def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def add(a, b, c):
    return a + b + c


def print_result(result):
    print(f"Result: {result}")


apply_async(add, [1, 2, 1], callback=print_result)


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print(f"[{sequence}] : {result}")
    return handler


hand = make_handler()

apply_async(add, [1, 2, 1], callback=hand)
apply_async(add, [1, 5, 1], callback=hand)
apply_async(add, [1, 7, 1], callback=hand)

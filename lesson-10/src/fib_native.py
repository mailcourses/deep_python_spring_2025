
def fib_rec_py(n: int) -> int:
    if n < 3:
        return 1

    return fib_rec_py(n - 1) + fib_rec_py(n - 2)


def fib_iter_py(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a

def cached(func):
    cache = {}

    def benchmark(a, b):
        if (a, b) in cache:
            return 1, cache[(a, b)]

        func_value = func(a, b)
        cache[(a, b)] = func_value
        return 0, func_value

    return benchmark


@cached
def sub(a, b):
    return a - b



def cache_decorator(func):
    memo = {}

    def wrapper_memo(*args, **kwargs):
        if args in memo:
            return memo[args]
        else:
            result = func(*args, **kwargs)
            memo[args] = result
            return result
    return wrapper_memo


@cache_decorator
def add(a, b):
    return a + b


print(add(2, 4))
print(add(8, 2))
print(add(2, 4))

def result_cache_decorator(func):
    cache = {}  # The dictionary to store the function's results and then saving them in the cache for future use

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))  # frozenset -- to avoid TypeError: unhashable type: 'dict' with kwargs
        if key in cache:  # checking if the dictionary already has the value
            print("Cached result is used: ")
            return cache[key]
        else:
            print("Calculation performed: ")
            res = func(*args, **kwargs)
            cache[key] = res
            return res

    return wrapper


@result_cache_decorator
def simple(a, b):
    return a + b


# Testing:
print(simple(2, 3))  # Calculation performed
print(simple(2, 3))  # Cached result is used
print(simple(a=2, b=3))  # Calculation performed
print(simple(a=2, b=3))  # Cached result is used
print(simple(b=3, a=2))  # Cached result is used
print(simple(9, 18))  # Calculation performed


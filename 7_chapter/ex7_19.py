import functools

from ex7_17 import clock

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(6))

# functools.lru_cache(maxsize=128, typed=False)
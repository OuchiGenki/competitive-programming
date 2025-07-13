from functools import lru_cache

@lru_cache
def f(x):
    if x == 0:
        return 1
    return f(int(x/2)) + f(int(x/3))

n = int(input())
print(f(n))
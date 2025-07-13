from functools import cache

@cache
def f(x):
    if x == 1:
        return 0
    return f(x//2) + f((x+1)//2) + x

N = int(input())
print(f(N))
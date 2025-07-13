import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
zero = 1
one = n

while (one-zero) > 1:
    mid = (one+zero) // 2
    print("?", mid, flush=True)
    s = int(input())
    
    if s == 0:
        zero = mid
    else:
        one = mid

print("!", zero, flush=True)
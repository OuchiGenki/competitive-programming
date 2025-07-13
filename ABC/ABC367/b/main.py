import sys
sys.setrecursionlimit(10**8)

x = float(input())

if x.is_integer():
    print(int(x))
else:
    print(x)
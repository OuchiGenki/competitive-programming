import sys
sys.setrecursionlimit(10**8)

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(sum(a)-sum(b)+1)
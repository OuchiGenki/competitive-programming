import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] % 2 == 0:
        print(a[i], end=" ")
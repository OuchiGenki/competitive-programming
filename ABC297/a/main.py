import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, d = map(int, input().split())
t = list(map(int, input().split()))

ans = -1
for i in range(1, n):
    if t[i]-t[i-1] <= d:
        ans = t[i]
        break

print(ans)
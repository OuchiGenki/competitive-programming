import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = dict()
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

ans = 0
for i in d:
    ans += d[i]//2

print(ans)
import itertools
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
m = int(input())
ng = []
for i in range(m):
    x, y = map(int, input().split())
    ng.append((x-1, y-1))
    ng.append((y-1, x-1))
arr = [i for i in range(n)]

ans = 1<<60
# i: junban   p[i]: hito
for p in itertools.permutations(arr):
    skip = False
    time = 0
    for i in range(n):
        if i < n-1 and (p[i], p[i+1]) in ng:
            skip = True
            break
        time += a[p[i]][i]
    if skip:
        continue
    ans = min(ans, time)

if ans == 1<<60:
    print(-1)
else:
    print(ans)
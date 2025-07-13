from collections import defaultdict

N = int(input())
d = defaultdict(list)
for i in range(N):
    f, s = map(int, input().split())
    d[f].append(s)

ans = 0
U = []
for v in d.values():
    U.append(max(v))
    if len(v) < 2:
        continue
    v.sort(reverse=True)
    ans = max(ans, v[0]+v[1]//2)
U.sort(reverse=True)

if len(U) >= 2:
    ans = max(ans, U[0] + U[1])
print(ans)
from collections import defaultdict

N, L = map(int, input().split())

if L % 3 != 0:
    print(0)
    exit()

d = list(map(int, input().split()))
pos = defaultdict(int)
pos[0] += 1
p = 0
for i in range(N-1):
    p += d[i]
    pos[p % L] += 1

ans = 0
for i in range(L//3):
    ans += pos[i] * pos[i+L//3] * pos[i+L//3+L//3]

print(ans)
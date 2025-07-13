N, M = map(int, input().split())

s = set()
for i in range(M):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    if u == v:
        continue
    s.add((u, v))

print(M-len(s))

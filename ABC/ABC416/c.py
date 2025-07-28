from itertools import product

n, k, x = map(int, input().split())
S = [input() for _ in range(n)]
res = []
for p in product(range(n), repeat=k):
    now = ''
    for i in range(k):
        now += S[p[i]]
    res.append(now)
res.sort()
print(res[x-1])

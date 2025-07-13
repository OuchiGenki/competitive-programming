n, m = map(int, input().split())
g = [[] for i in range(n)]
seen = [0 for i in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

def dfs(tg):
    seen[tg] = 1
    for next_tg in g[tg]:
        if seen[next_tg] == 1: continue
        dfs(next_tg)

ans = 0
for i in range(n):
    if seen[i] == 1: continue
    dfs(i)
    ans += 1

print(ans)
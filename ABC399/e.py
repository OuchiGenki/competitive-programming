from collections import defaultdict

N = int(input())
S = input()
T = input()

edges= list(set([(s, t) for s, t in zip(S, T)]))

G = defaultdict(list)
RG = defaultdict(list)
for u, v in edges:
    G[u].append(v)
    RG[v].append(u)

def dfs(v, G, visited):
    global cycle, cnt
    visited[v] = True
    for nv in RG[v]:
        if not visited[nv]:
            cnt += 1
            dfs(nv, G, visited)
        else:
            cycle = True
    return visited

visited = defaultdict(bool)
for v in G.keys():
    visited[v] = False

cycle = False
cnt = 0
for v in list(RG.keys()):
    print(v, len(G[v]))
    if not visited[v] and len(G[v]) == 0:
        print(v)
        dfs(v, RG, visited)

print(RG)
if cycle:
    print(-1)
else:
    print(cnt)

N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(N):
    G[i].append(A[i]-1)

v = 0
visited = [False] * N
visited[0] = True
path = []
while True:
    visited[v] = True
    path.append(v)
    v = G[v][0]
    if visited[v]:
        start = v
        break

ans = []
flag = False
for i in range(len(path)):
    if path[i] == start:
        flag = True
    if flag:
        ans.append(path[i]+1)

print(len(ans))
print(*ans)

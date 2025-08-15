n, m = map(int, input().split())
E = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    E[a-1][b-1] = c
ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            E[i][j] = min(E[i][j], E[i][k] + E[k][j])
            if E[i][j] != float('inf') and i != j:
                ans += E[i][j]
print(ans)
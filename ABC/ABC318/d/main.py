n = int(input())
D = []
for i in range(n-1):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        D.append((lst[j], i, i+1+j))
D.sort(reverse=True)
used = [False for i in range(n)]
ans = 0
for i in range(len(D)):
    d, u, v = D[i]
    if used[u] or used[v]:
        continue
    ans += d
    used[u] = True
    used[v] = True
print(D)
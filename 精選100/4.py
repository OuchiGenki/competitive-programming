n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
point = []
for i in range(m):
    for j in range(m):
        sum = 0
        if i == j:
            continue
        for k in range(n):
            sum += max(a[k][i], a[k][j])
        point.append(sum)
print(max(point))
n, m = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
D = []
for i in range(n-1):
    D.append(X[i+1] - X[i])
D.sort()
ans = 0
for i in range(n-m):
    ans += D[i]
print(ans)
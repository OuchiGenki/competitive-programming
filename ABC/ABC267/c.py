n, m = map(int, input().split())
A = list(map(int, input().split()))
cum = [0]
for i in range(n):
    cum.append(cum[-1] + A[i])
ans = 0
for i in range(m):
    ans += (i+1) * A[i]
now = ans
for i in range(m, n):
    now -= cum[i] - cum[i-m]
    now += m * A[i]
    ans = max(ans, now)
print(ans)
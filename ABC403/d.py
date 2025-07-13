from collections import defaultdict

def solve(lst):
    M = len(lst)
    dp = [[0] * 2 for i in range(M+1)]
    for i in range(M):
        dp[i+1][0] = max(dp[i+1][0], dp[i][1] + lst[i])
        dp[i+1][1] = max(dp[i+1][1], dp[i][0])
        dp[i+1][1] = max(dp[i+1][1], dp[i][1])
    return sum(lst) - max(dp[M][0], dp[M][1])


N, D = map(int, input().split())
A = list(map(int, input().split()))

if D == 0:
    print(N - len(set(A)))
    exit()

cnt = defaultdict(int)
for i in range(N):
    cnt[A[i]] += 1

ans = 0
groups = [[] for i in range(D)]

for i in range(max(A)+1):
    groups[i%D].append(cnt[i])

for row in groups:
    ans += solve(row)

print(ans)
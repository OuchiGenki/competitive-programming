from collections import defaultdict

def solve(lst):
    M = len(lst)
    dp = [[0] * 2 for i in range(M+1)]
    for i in range(M):
        dp[i+1][0] = max(dp[i+1][0], max(dp[i][0], dp[i][1]))
        dp[i+1][1] = max(dp[i+1][1], dp[i][0] + lst[i])
    return sum(lst) - max(dp[M])


N, D = map(int, input().split())
A = list(map(int, input().split()))　

if D == 0:
    print(N - len(set(A)))
    exit()

cnt = defaultdict(int)
for i in range(N):
    cnt[A[i]] += 1

max_A = max(A)
ans = 0
for i in range(D):
    lst = []
    for j in range(i, max_A+1, D):
        lst.append(cnt[j])
    ans += solve(lst)

print(ans)
N, M = map(int, input().split())
D = [1 for i in range(M+1)]
for i in range(N):
    l, r = map(int, input().split())
    D[r] = max(D[r], l+1)

ans = 0
for i in range(1, M+1):
    D[i] = max(D[i], D[i-1])
    ans += i - D[i] + 1

print(ans)
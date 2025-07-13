N, M = map(int, input().split())
cnt = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    cnt[(a+b) % N] += 1

ans = M * (M-1) // 2
for i in range(N):
    ans -= cnt[i] * (cnt[i] - 1) // 2

print(ans)
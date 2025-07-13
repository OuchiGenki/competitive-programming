N, M = map(int, input().split())
A = list(map(int, input().split()))
length = max(A)

R = [0]
for i in range(2*N-1):
    R.append((R[-1] + A[i % N]) % M)

cnt = [0 for i in range(M)]
for i in range(N):
    cnt[R[i] % M] += 1

ans = 0
for i in range(N, 2*N):
    cnt[R[i - N] % M] -= 1
    ans += cnt[R[i] % M]
    cnt[R[i] % M] += 1

print(ans)
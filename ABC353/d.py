MOD = 998244353
n = int(input())
A = list(map(int, input().split()))
D = list(map(lambda x: len(str(x)), A))
cumsum = [0]
for i in range(n):
    cumsum.append(cumsum[-1] + A[i])

ans = 0
for j in range(1, n):
    ans += 10**(D[j]) * (cumsum[j]) + j * A[j]
    ans %= MOD
print(ans)
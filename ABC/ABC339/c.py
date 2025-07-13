N = int(input())
A = list(map(int, input().split()))
cumsum = [0]
for i in range(N):
    cumsum.append(cumsum[i] + A[i])
min_cumsum = min(cumsum)
print(cumsum[N] - min_cumsum)
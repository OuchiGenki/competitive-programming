from sortedcontainers import SortedList

N, K = map(int, input().split())
P = list(map(int, input().split()))
idx = {P[i]: (i+1) for i in range(N)}
P.sort()
S = SortedList([idx[P[i]] for i in range(K)])

res = float('inf')
for i in range(N-K+1):
    min_idx = S[0]
    max_idx = S[-1]
    res = min(res, max_idx-min_idx)
    S.discard(idx[P[i]])
    if i+K < N:
        S.add(idx[P[i+K]])

print(res)
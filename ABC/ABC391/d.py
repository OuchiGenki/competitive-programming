from collections import defaultdict

N, W = map(int, input().split())
X, Y = [], []
cnt = [0 for i in range(W)]
layer = [0 for i in range(N)]
r = defaultdict(int)
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    cnt[x-1] += 1
    layer[i] = cnt[x-1]
    r[layer[i]] = max(r[layer[i]], y)
min_cnt = min(cnt)
Q = int(input())

for i in range(Q):
    t, a = map(int, input().split())
    if layer[a-1] > min_cnt:
        print('Yes')
        continue
    if r[layer[a-1]] <= t:
        print('No')
    else:
        print('Yes')

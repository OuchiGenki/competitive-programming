from collections import defaultdict

N, T = map(int, input().split())
points = [0 for i in range(N)]
cnt = defaultdict(int)
cnt[0] += N

now = 1
res = []
for i in range(T):
    a, b = map(int, input().split())
    before = points[a-1]
    after = points[a-1] + b

    cnt[before] -= 1
    cnt[after] += 1
    points[a-1] = after

    if cnt[before] == 0:
        now -= 1
    if cnt[after] == 1:
        now += 1
    
    res.append(now)
    
for i in res:
    print(i)
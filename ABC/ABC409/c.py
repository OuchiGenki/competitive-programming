from collections import defaultdict

N, L = map(int,input().split())
d = list(map(int,input().split()))

if L % 3 != 0:
    print(0)
    exit()

cum = [0]
for i in range(N-1):
    cum.append((cum[i]+d[i]) % L)
dots = []
for i in range(N):
    dots.append(cum[i]%L)

cnt = defaultdict(int)
for i in range(N):
    cnt[dots[i]] += 1

ans = 0
c = set()
for i in range(N):
    l = L//3
    d1 = dots[i]
    d2 = (dots[i]+l) % L
    d3 = (dots[i]+l+l) % L
    d1, d2, d3 = sorted([d1, d2, d3])
    if (d1, d2, d3) not in c:
        ans += cnt[d1]*cnt[d2]*cnt[d3]
        c.add((d1, d2, d3))

print(ans)
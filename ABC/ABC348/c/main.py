from collections import defaultdict

N = int(input())
d = defaultdict(lambda: float('inf'))

for i in range(N):
    a, c = map(int, input().split())
    d[c] = min(d[c], a)

print(max(d.values()))
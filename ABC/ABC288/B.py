n, k = map(int, input().split())
s = [input() for i in range(n)]
ranker = sorted(s[0:k])
for p in ranker:
    print(p)
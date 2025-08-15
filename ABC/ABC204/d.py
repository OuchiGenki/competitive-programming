n = int(input())
T = list(map(int, input().split()))
sumT = sum(T)
S = set([0])
for i in range(n):
    SS = set()
    for j in S:
        SS.add(j + T[i])
    S |= SS
ans = float('inf')
for s in S:
    t = sumT - s
    ans = min(ans, max(s, t))
print(ans)
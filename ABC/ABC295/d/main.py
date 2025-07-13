import sys
sys.setrecursionlimit(10**8)

s = list(map(int, input()))
cnt = [[0 for i in range(10)] for j in range(len(s)+1)]

d = {tuple([0 for i in range(10)]): 1}
for i in range(len(s)):
    x = s[i]
    for j in range(10):
        cnt[i+1][j] = cnt[i][j]
    cnt[i+1][x] += 1
    cnt[i+1][x] %= 2
    if tuple(cnt[i+1]) not in d:
        d[tuple(cnt[i+1])] = 1
    else:
        d[tuple(cnt[i+1])] += 1

ans = 0
for i in d:
    x = d[i]
    ans += x*(x-1)//2
print(ans)
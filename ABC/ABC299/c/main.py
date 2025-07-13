import sys
sys.setrecursionlimit(10**8)

n = int(input())
s = list(input())

ans = -1
score = 0
for i in range(n):
    if s[i] == '-':
        ans = max(ans, score)
        score = 0
    else:
        score += 1

s.reverse()
score = 0
for i in range(n):
    if s[i] == '-':
        ans = max(ans, score)
        score = 0
    else:
        score += 1

if ans == 0:
    print(-1)
else:
    print(ans)
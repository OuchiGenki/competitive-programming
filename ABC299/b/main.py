import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

max_score = -1
ans = -1
for i in range(n):
    if c[i] == t:
        if r[i] > max_score:
            ans = i+1
            max_score = r[i]

if ans == -1:
    t = c[0]
    for i in range(n):
        if c[i] == t:
            if r[i] > max_score:
                ans = i+1
                max_score = r[i]

print(ans)
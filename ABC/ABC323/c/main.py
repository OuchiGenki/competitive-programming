import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [input() for i in range(n)]

max_points = 0
score_list = [0 for i in range(n)]
not_earned = [[] for i in range(n)]

for i in range(n):
    points = i+1
    for j in range(m):
        if s[i][j] == "o":
            points += a[j]
        else:
            not_earned[i].append(a[j])
    score_list[i] = points
    if max_points < points:
        max_points = points

for i in range(n):
    not_earned[i].sort(reverse=True)

for i in range(n):
    ans = 0
    while max_points > score_list[i]:
        score_list[i] += not_earned[i][ans]
        ans += 1
    print(ans)
    
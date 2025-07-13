from collections import defaultdict

N = int(input())
H = list(map(int, input().split()))

s = set(H)
answer = 0

def f(d):
    max_streak = 0
    height = -1
    for i in range(d):
        streak = 0
        for j in range(i, N, d):
            if H[j] != height:
                streak = 0
                height = H[j]
            streak += 1
            max_streak = max(max_streak, streak)
    return max_streak

for d in range(1, N+1):
    result = f(d)
    answer = max(answer, result)

print(answer)
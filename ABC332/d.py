from itertools import permutations

h, w = map(int, input().split())
A = [list(map(int, input().split())) for i in range(h)]
B = [list(map(int, input().split())) for i in range(h)]
ans = float('inf')
for P in permutations([i for i in range(h)]):
    for Q in permutations([i for i in range(w)]):
        flag = True
        for i in range(h):
            for j in range(w):
                if A[P[i]][Q[j]] != B[i][j]:
                    flag = False
        if not flag:
            continue

        now = 0
        for i in range(h):
            for j in range(i+1, h):
                if P[i] > P[j]:
                    now += 1
        for i in range(w):
            for j in range(i+1, w):
                if Q[i] > Q[j]:
                    now += 1
        ans = min(ans, now)

if ans == float('inf'):
    print(-1)
else:
    print(ans)